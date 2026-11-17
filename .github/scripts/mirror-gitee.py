import hashlib
import json
import os
import pathlib
import re
import subprocess
import tempfile
import time
import urllib.error
import urllib.request

SOURCE = '2716190547/zmark-releases'
TARGET = 'https://gitee.com/api/v5/repos/zeng_sc/zmark-releases'
TOKEN = os.environ['GITEE_TOKEN']
HEADERS = {'Authorization': f'Bearer {TOKEN}', 'User-Agent': 'zmark-release-mirror'}


def api(path, data=None, method=None, content_type=None):
    headers = dict(HEADERS)
    if content_type:
        headers['Content-Type'] = content_type
    request = urllib.request.Request(TARGET + path, data=data, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.load(response)



def upload_asset(release_id, path):
    config = ''.join(f'header = {json.dumps(f"{name}: {value}")}\n' for name, value in HEADERS.items())
    result = subprocess.run([
        'curl', '--silent', '--show-error', '--fail-with-body',
        '--connect-timeout', '20', '--max-time', '120', '--config', '-',
        '--form', f'file=@{path};type=application/octet-stream',
        f'{TARGET}/releases/{release_id}/attach_files',
    ], input=config, text=True, capture_output=True, check=True)
    return json.loads(result.stdout)


def digest(data):
    return hashlib.sha256(data).digest()


def verified_asset(release, name, url, data):
    existing = next((asset for asset in (release.get('assets') or []) if asset.get('name') == name), None)
    if not existing:
        return False
    if existing.get('browser_download_url') != url:
        raise SystemExit(f'Unexpected mirror URL for {name}')
    with urllib.request.urlopen(url, timeout=120) as response:
        if digest(response.read()) != digest(data):
            raise SystemExit(f'Existing Gitee asset differs: {name}')
    return True


source_release = json.loads(subprocess.check_output(['gh', 'release', 'view', '--repo', SOURCE, '--json', 'tagName,body']))
tag = source_release['tagName']
if not re.fullmatch(r'v[0-9]+\.[0-9]+\.[0-9]+', tag):
    raise SystemExit(f'Unsupported release tag: {tag}')
version = tag[1:]
names = [f'ZMark-{version}.zip', f'ZMark-{version}-setup.exe', 'latest.json', 'latest-windows.json']
with tempfile.TemporaryDirectory() as directory:
    args = ['gh', 'release', 'download', tag, '--repo', SOURCE, '--dir', directory]
    for name in names:
        args.extend(['--pattern', name])
    subprocess.run(args, check=True)
    files = {name: (pathlib.Path(directory) / name).read_bytes() for name in names}
    try:
        release = api('/releases/tags/' + tag)
    except urllib.error.HTTPError as error:
        if error.code != 404:
            raise
        release = None
    if release is None:
        payload = json.dumps({'tag_name': tag, 'name': 'ZMark ' + tag, 'body': source_release.get('body') or 'ZMark release downloads mirrored from GitHub.', 'target_commitish': 'master'}).encode()
        release = api('/releases', payload, 'POST', 'application/json')
    for name, data in files.items():
        expected_url = f'https://gitee.com/zeng_sc/zmark-releases/releases/download/{tag}/{name}'
        if verified_asset(release, name, expected_url, data):
            print(f'Verified {name}')
            continue
        for attempt in range(3):
            try:
                asset = upload_asset(release['id'], pathlib.Path(directory) / name)
                if asset.get('browser_download_url') != expected_url:
                    raise SystemExit(f'Unexpected uploaded URL for {name}')
                break
            except (urllib.error.URLError, TimeoutError, subprocess.CalledProcessError) as error:
                release = api('/releases/tags/' + tag)
                if verified_asset(release, name, expected_url, data):
                    break
                if attempt == 2:
                    raise
                print(f'Upload failed for {name}; retrying: {error}')
                time.sleep(5 * (attempt + 1))
        release = api('/releases/tags/' + tag)
        if not verified_asset(release, name, expected_url, data):
            raise SystemExit(f'Uploaded asset not found: {name}')
        print(f'Uploaded {name}')

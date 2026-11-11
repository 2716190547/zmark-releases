import hashlib
import json
import os
import pathlib
import re
import subprocess
import tempfile
import urllib.error
import urllib.request
import uuid

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


def digest(data):
    return hashlib.sha256(data).digest()


tag = json.loads(subprocess.check_output(['gh', 'release', 'view', '--repo', SOURCE, '--json', 'tagName']))['tagName']
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
        payload = json.dumps({'tag_name': tag, 'name': 'ZMark ' + tag, 'body': 'ZMark release downloads mirrored from GitHub.', 'target_commitish': 'master'}).encode()
        release = api('/releases', payload, 'POST', 'application/json')
    for name, data in files.items():
        expected_url = f'https://gitee.com/zeng_sc/zmark-releases/releases/download/{tag}/{name}'
        existing = next((asset for asset in (release.get('assets') or []) if asset.get('name') == name), None)
        if existing:
            if existing.get('browser_download_url') != expected_url:
                raise SystemExit(f'Unexpected mirror URL for {name}')
            with urllib.request.urlopen(expected_url, timeout=120) as response:
                if digest(response.read()) != digest(data):
                    raise SystemExit(f'Existing Gitee asset differs: {name}')
            print(f'Verified {name}')
            continue
        boundary = 'zmark' + uuid.uuid4().hex
        prefix = f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{name}"\r\nContent-Type: application/octet-stream\r\n\r\n'.encode()
        body = prefix + data + f'\r\n--{boundary}--\r\n'.encode()
        asset = api(f'/releases/{release["id"]}/attach_files', body, 'POST', f'multipart/form-data; boundary={boundary}')
        if asset.get('browser_download_url') != expected_url:
            raise SystemExit(f'Unexpected uploaded URL for {name}')
        print(f'Uploaded {name}')

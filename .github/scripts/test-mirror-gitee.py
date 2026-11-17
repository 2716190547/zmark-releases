"""Exercise the production upload helper without running the live mirror."""
import ast
import http.server
import json
import pathlib
import subprocess
import tempfile
import threading
import unittest


class UploadTest(unittest.TestCase):
    def test_curl_posts_the_file_and_keeps_credentials_out_of_arguments(self):
        source = pathlib.Path(__file__).with_name('mirror-gitee.py').read_text()
        function = next(node for node in ast.parse(source).body
                        if isinstance(node, ast.FunctionDef) and node.name == 'upload_asset')
        received = {}

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_POST(self):
                received['path'] = self.path
                received['auth'] = self.headers.get('Authorization')
                received['body'] = self.rfile.read(int(self.headers['Content-Length']))
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(b'{"browser_download_url":"verified-upload"}')

            def log_message(self, *args):
                pass

        server = http.server.HTTPServer(('127.0.0.1', 0), Handler)
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        try:
            headers = {'Authorization': 'Bearer test-only-placeholder'}
            namespace = {'json': json, 'subprocess': subprocess, 'HEADERS': headers,
                         'TARGET': f'http://127.0.0.1:{server.server_port}'}
            exec(compile(ast.Module(body=[function], type_ignores=[]), 'mirror-gitee.py', 'exec'), namespace)
            with tempfile.TemporaryDirectory() as directory:
                file = pathlib.Path(directory) / 'package.zip'
                file.write_bytes(b'\x00exact-package-bytes\xff')
                from unittest.mock import patch
                with patch.object(subprocess, 'run', wraps=subprocess.run) as run:
                    result = namespace['upload_asset'](42, file)
                self.assertNotIn('test-only-placeholder', ' '.join(run.call_args.args[0]))
            self.assertEqual(result, {'browser_download_url': 'verified-upload'})
            self.assertEqual(received['path'], '/releases/42/attach_files')
            self.assertEqual(received['auth'], headers['Authorization'])
            self.assertIn(b'name="file"; filename="package.zip"', received['body'])
            self.assertIn(b'\x00exact-package-bytes\xff', received['body'])
        finally:
            server.shutdown()
            worker.join()
            server.server_close()


if __name__ == '__main__':
    unittest.main()

from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)
BASE_DIR = os.getcwd()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_file(path):
    if path == "" or path.endswith('/'):
        path = os.path.join(path, 'index.html')

    file_path = os.path.join(BASE_DIR, path)

    if os.path.exists(file_path) and os.path.isfile(file_path):
        return send_from_directory(BASE_DIR, path)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
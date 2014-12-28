import urllib

from flask import Flask, request, jsonify

from lightshot.S3 import S3
from lightshot.screenshot import Screenshot


debug = True

app = Flask(__name__)
app.config.from_envvar('LIGHTSHOT_SETTINGS')


@app.route("/generate")
def generate():
    url = request.args.get('url', '')
    url = urllib.unquote(url).decode('utf8')

    screenshot = Screenshot(url)
    filename = screenshot.capture()

    response = {'success': True, 'path': filename}

    upload_to_s3 = app.config['S3_UPLOAD']

    if upload_to_s3:
        s3 = S3(app.config['S3_ACCESS_KEY'], app.config['S3_SECRET_KEY'], app.config['S3_BUCKET'])
        s3_url = s3.upload_file(screenshot, public_read=True)
        screenshot.delete_local_file()
        response['s3_url'] = s3_url
        del response['path']

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)

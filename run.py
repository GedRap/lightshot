from flask import Flask, request, jsonify
import urllib
from app.mod_lightshot.models import Screenshot
from app.mod_lightshot.S3 import S3

debug = True

app = Flask(__name__)
app.config.from_envvar('LIGHTSHOT_SETTINGS')

@app.route("/generate")
def generate():
  url = request.args.get('url', '')
  url = urllib.unquote(url).decode('utf8')
  
  screenshot = Screenshot(url)
  filename = screenshot.capture()

  s3 = S3(app.config['S3_ACCESS_KEY'], app.config['S3_SECRET_KEY'], app.config['S3_BUCKET'])
  s3.upload_file(screenshot, public_read=True)
  
  return jsonify(success=True, path=filename)

if __name__ == "__main__":
  app.run(debug=True)

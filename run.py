from flask import Flask, request, jsonify
import urllib
from app.mod_lightshots.models import Screenshot

debug = True

app = Flask(__name__)

@app.route("/generate")
def generate():
  url = request.args.get('url', '')
  url = urllib.unquote(url).decode('utf8')
  
  screenshot = Screenshot(url)
  filename = screenshot.capture()
  
  return jsonify(success=True, path=filename)

if __name__ == "__main__":
  app.run(debug=True)

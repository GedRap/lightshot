from flask import Flask, request, jsonify
import time
import re
from ghost import Ghost
import urllib

debug = True

app = Flask(__name__)

@app.route("/generate")
def generate():
  url = request.args.get('url', '')
  url = urllib.unquote(url).decode('utf8')
  filename = "shots/" + generate_filename(url)
  save_screenshot(url, filename)
  return jsonify(success=True, path=filename)

def generate_filename(url):
  stripped_url = re.sub(r'\W+', '', url)
  timestamp = int(time.time())

  return str(timestamp) + "_" + stripped_url + ".jpg"

def save_screenshot(url, path):
  ghost = Ghost(wait_timeout=120)
  page, extra = ghost.open(url)
  ghost.capture_to(path)
 
if __name__ == "__main__":
  app.run(debug=True)

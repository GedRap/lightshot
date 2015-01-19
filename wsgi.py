import os
os.environ['LIGHTSHOT_SETTINGS'] = 'dev.config'

from lightshot import app
app.run(debug=True)
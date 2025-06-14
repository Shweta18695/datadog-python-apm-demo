from flask import Flask
from ddtrace import patch_all

patch_all()  # auto-instrument everything

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Datadog!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

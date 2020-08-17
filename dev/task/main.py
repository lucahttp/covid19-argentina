# [START gae_python38_app]
# example from
# https://smirnov-am.github.io/background-jobs-with-flask/
# and this
# https://gcpexp.com/posts/minimal-flask-app-gae/
# and this
# https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/appengine/standard_python3/hello_world
# 
import os
import time
from flask import Flask, jsonify
from threading import Thread
from tasks import threaded_task

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
app.secret_key = os.urandom(42)



@app.route('/hello')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route("/", defaults={'duration': 5})
@app.route("/<int:duration>")
def index(duration):
    thread = Thread(target=threaded_task, args=(duration,))
    thread.daemon = True
    thread.start()
    return jsonify({'thread_name': str(thread.name),
                    'started': True})


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
    #app.run(debug=True, use_reloader=True)
# [END gae_python38_app]








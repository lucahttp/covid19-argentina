from flask import Flask
import requests

import time
app = Flask(__name__)


from multiprocessing import Process

@app.route('/render/<id>', methods=['POST','GET'])
def render_script(id=None):
    ...
    heavy_process = Process(  # Create a daemonic process with heavy "my_func"
        target=my_func,
        daemon=True
    )
    heavy_process.start()
    dataso = "GG"
    response = app.response_class(
        response= dataso,
        #response=data,
        status=200,
        mimetype='text/plain'
    )
    return response

# Define some heavy function
def my_func():
    time.sleep(10)
    print("Process finished")

if __name__=='__main__':
    app.run(debug=True, use_reloader=True)
from flask import Flask
import requests
import time
from multiprocessing import Process
import datetime
from flask import g




player = None
data = None
oldData = None





def myfunc():
    print("Hello my name is " + g.data)

def setData():
    g.oldData = g.data
    g.data = str(datetime.datetime.now())
    #str(datetime.datetime.now().replace(microsecond=00))

#mydata.myfunc()
print("GG")


app = Flask(__name__)



@app.route('/render/', methods=['POST','GET'])
def render_script():
    ...
    heavy_process = Process(  # Create a daemonic process with heavy "my_func"
        target=my_func,
        daemon=True
    )
    heavy_process.start()
    dataso = "g.data+g.oldData"
    response = app.response_class(
        response= dataso,
        #response=data,
        status=200,
        mimetype='text/plain'
    )
    return response

# Define some heavy function
def my_func():
    time.sleep(1)
    print("Process finished")
    #setData()
    print("data()oldData")

if __name__=='__main__':
    #app.run(debug=True, use_reloader=True)
    app.run(debug=True, use_reloader=True)
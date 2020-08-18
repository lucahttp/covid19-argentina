from flask import Flask
import requests

import time
app = Flask(__name__)


class Data:
    def __init__(self, initial):
        self.data = initial
        self.oldData = "no hay nada"

    def myfunc(self):
        print("Hello my name is " + self.data)

    def getData(self):
        return self.data

    def getOldData(self):
        return self.oldData

    def setData(self,data):
        self.oldData = self.data
        self.data = str(data)



mydata = Data("viejo dato")
mydata.myfunc()



from multiprocessing import Process

@app.route('/<somedata>', methods=['GET'])
def render_script(somedata=None):
    ...
    heavy_process = Process(  # Create a daemonic process with heavy "my_func"
        target=my_func(somedata),
        daemon=True
    )
    heavy_process.start()
    """
    return Response(
        mimetype='application/json',
        status=200
    )
    """   
    dataso = '{ "Data":"'+mydata.getData()+'", "Old Data":"'+mydata.getOldData()+'"}'
    response = app.response_class(
        response= dataso,
        #response=data,
        status=200,
        mimetype='application/json'
    )
    return response

# Define some heavy function
def my_func(inporteddata):
    print("Process finished")
    mydata.setData(inporteddata)



if __name__=='__main__':
    app.run(debug=True, use_reloader=True)
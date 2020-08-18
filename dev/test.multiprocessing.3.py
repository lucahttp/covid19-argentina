from flask import Flask
import requests

import time
app = Flask(__name__)


responsecode = None

import requests
def download(url,filefolder):

    myfile = requests.get(url, allow_redirects=True)

    open(filefolder, 'wb').write(myfile.content)
    pass


def downloadCSV():
    #Downloader
    # https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
    url = "https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.csv"

    import os
    directory = './data/'
    if not os.path.exists(directory):
        os.makedirs(directory)
        download(url,'./data/casoscovid19.csv')
    pass

# Define some heavy function
def my_func():
    #time.sleep(10)
    downloadCSV()
    print("Process finished")

from multiprocessing import Process

@app.route('/render/<id>', methods=['GET'])
def render_script(id=None):
    ...
    heavy_process = Process(  # Create a daemonic process with heavy "my_func"
        target=my_func,
        daemon=True
    )
    heavy_process.start()
    """
    return Response(
        mimetype='application/json',
        status=200
    )
    """   
    response = app.response_class(
        response="GG",
        #response=data,
        status=200,
        mimetype='application/json'
    )
    return response




if __name__=='__main__':
    app.run(debug=True, use_reloader=True)
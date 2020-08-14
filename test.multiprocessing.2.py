from multiprocessing import Pool
from flask import Flask

app = Flask(__name__)
_pool = None

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

def expensive_function(x):
    # import packages that is used in this function
    # do your expensive time consuming process
    downloadCSV()
    return x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x

@app.route('/')
def gg():
        x=1
        f = _pool.apply_async(downloadCSV(),[x])
        r = f.get(timeout=2)
        return 'Result is %d'%r

@app.route('/expensive_calc/<int:x>')
def route_expcalc(x):
        f = _pool.apply_async(expensive_function,[x])
        r = f.get(timeout=2)
        return 'Result is %d'%r

if __name__=='__main__':
        _pool = Pool(processes=4)
        try:
            # insert production server deployment code
            app.run(debug=True, use_reloader=True)
        except KeyboardInterrupt:
            _pool.close()
            _pool.join()

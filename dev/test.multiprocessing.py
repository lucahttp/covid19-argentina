from multiprocessing import Pool
from flask import Flask

app = Flask(__name__)
_pool = None

def double_f(x):
    return x*x

def expensive_function(gg):
    #response = requests.get('https://google.com/')
    #response = requests.get('http://34.82.12.150\random.5.php')

    import requests

    url = "http://34.82.12.150/random.5.php"

    payload = {'random': ''}
    files = []
    headers= {}
    response = requests.request("POST", url, headers=headers, data = payload, files = files)

    print(response.text.encode('utf8'))
    print(response.status_code)

    return "asd"+str(gg)

@app.route('/double_calc/<int:x>')
def expcalc(x):
    
    f = _pool.map(expensive_function, range(1))
    #f = _pool.apply_async(double_f,[x])
    #r = f.get(timeout=2)
    return 'Result is'+str(f)

if __name__=='__main__':
    _pool = Pool(processes=4)
    try:
        app.run(debug=True, use_reloader=True)

    except KeyboardInterrupt:
        _pool.close()
        _pool.join()
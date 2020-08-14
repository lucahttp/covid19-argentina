from multiprocessing import Pool
from flask import Flask

app = Flask(__name__)
_pool = None

def expensive_function(x):
    # import packages that is used in this function
    # do your expensive time consuming process
    return x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x

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

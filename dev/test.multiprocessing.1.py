from multiprocessing import Pool
from flask import Flask
from flask import jsonify
import ast
import pandas as pd
import requests
 
app = Flask(__name__)
_pool = None
 
# Function that run multiple tasks
def get_response(x):
    """returns response for URL list"""
    m = requests.get((x),verify=False)
    return m.text
tasks = print("GG")

@app.route('/call-me/')
def health_check():
    """returns pandas dataframe into HTML for health-check Services"""
    resp_pool = _pool.map(get_response,tasks)
    table_frame= pd.DataFrame([ast.literal_eval(resp) for resp in resp_pool])
    return table_frame.to_html()
    
if __name__=='__main__':
    _pool = Pool(processes=12) # this is important part- We
    try:
        # insert production server deployment code
        app.run(debug=True, use_reloader=True)

    except KeyboardInterrupt:
        _pool.close()
        _pool.join()
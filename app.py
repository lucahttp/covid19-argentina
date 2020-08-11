from flask import json
from flask import Flask

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:


app = Flask(__name__)

#data = 'hola : luca'

def make_summary():
    data = y
    data = 'hola : luca'
    return data

@app.route('/')
def summary():
    data = make_summary()
    response = app.response_class(
        #response=json.dumps(data),
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)

# c:\python27\python.exe -m pip install --upgrade pip
# c:\python38\python.exe -m pip install --upgrade pip
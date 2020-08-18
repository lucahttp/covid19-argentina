# C:/Python38/python.exe -m pip install quart
from quart import Quart, websocket, render_template

app = Quart(__name__)

def make_response(gg):
    print("asdasd")
    pass 

@app.route("/")
async def hello2():
    return {"Hello": "World!"}


@app.websocket('/ws')
async def ws():
    while True:
        await websocket.send('hello')

@app.route("/hello/<name>")  # example.com/hello/quart
async def hello(name):
    return f"Hello, {name}!"

@app.route("/cook")
async def cook():
    response = await make_response("Hello")
    response.set_cookie("name", "value")
    return response

if __name__ == "__main__":
    app.run(debug=True)
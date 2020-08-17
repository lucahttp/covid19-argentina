from quart import Quart

app = Quart(__name__)

@app.route('/')
async def hello():
    data = 'hello from Quart/Flask as an async function'  
    response = app.response_class(
        response=data,
        status=200,
        mimetype='text/plain'
        # text/plain, text/html, text/css, text/javascript application/json
        # https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_types
    )
    return response


app.debug = True
#app.run(host="0.0.0.0",port=80)
app.run(debug=True, use_reloader=True)
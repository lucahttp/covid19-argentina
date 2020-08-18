# C:/Python38/python.exe -m pip install quart
from quart import Quart, websocket, render_template
import asyncio
app = Quart(__name__)

@app.route("/")
async def hello2():
    print("gg")
    return {"Hello": "asdasdas!"}


async def io_background_task():
    print("gg1")
    pass

async def cpu_background_task():
    print("gg2")
    pass

@app.route('/test')
async def create_job():
    # Runs in this event loop
    asyncio.ensure_future(io_background_task())

    # Runs on another thread
    asyncio.get_running_loop().run_in_executor(None, cpu_background_task())
    return 'Success'

if __name__ == "__main__":
    app.run(debug=True)
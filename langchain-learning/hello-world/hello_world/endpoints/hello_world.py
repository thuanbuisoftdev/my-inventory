from hello_world.app import app


@app.get("/")
def hello_world():
    return {"message": "Hello World"}

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/foo/bar")
async def view():
    return {"message": "bar!"}


@app.get("/foo/{bar}")
async def view(bar):
    return {"message": bar}

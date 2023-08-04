from enum import Enum

from fastapi import FastAPI


class ModelLetter(str, Enum):
    alpha = "alpha"
    beta = "beta"
    gamma = "gamma"


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


@app.get("/letter/{model_letter}")
async def view(model_letter: ModelLetter):
    if model_letter is ModelLetter.alpha:
        return {"model_letter": model_letter, "message": "Deep Learning FTW!"}

    if model_letter.value == "beta":
        return {"model_letter": model_letter, "message": "LeCNN all the images"}

    return {"model_letter": model_letter, "message": "Have some residuals"}

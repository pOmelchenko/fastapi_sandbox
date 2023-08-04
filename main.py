from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel


class ModelLetter(str, Enum):
    alpha = "alpha"
    beta = "beta"
    gamma = "gamma"


app = FastAPI()


class Message(BaseModel):
    message: str


@app.get("/")
async def root() -> Message:
    return Message(message="Hello world!")


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


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def read_user_item(
        item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item

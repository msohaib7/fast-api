from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get('/item')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published items
    if published:
        return {'data': f'{limit} published items from the db'}
    else:
        return {'data': f'{limit} items from the db'}



@app.get('/item/{id}')
def show(id: int):
    # fetch item with id = id
    return {'data': id}


# @app.get('/item/{id}/comments')
# def comments(id, limit=10):
#     # fetch comments of item with id = id
#     return {'data': {'1', '2'}}


class item(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/item')
def create_item(item: item):
    return {'data': f"item is created with title as {item.title}"}

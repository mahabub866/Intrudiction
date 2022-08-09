from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/") 
def read_root():
    return {"data": {'name':'Mahabub'}}


@app.get("/about")
def about():
   return {"data": {'about':'I am alwz loyal'}}
from fastapi import FastAPI
from todo.todo import todo_router

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to FastAPI!"}

app.include_router(todo_router) # todo_router를 app에 포함시킴 
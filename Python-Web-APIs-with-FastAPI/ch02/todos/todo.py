from fastapi import APIRouter

todo_router = APIRouter()
todo_list = []


@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)

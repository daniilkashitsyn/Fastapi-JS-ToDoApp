from fastapi import FastAPI
from app.tasks.tasks import router as tasks_router
from app.tasks.groups import router as groups_router
from app.users.router import router as users_router

app = FastAPI(
    title="ToDo"
)


@app.get("/")
def get_main():
    return "This is main page"


app.include_router(groups_router)
app.include_router(tasks_router)
app.include_router(users_router)

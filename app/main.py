from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.tasks.tasks import router as tasks_router
from app.tasks.groups import router as groups_router
from app.users.router import router as users_router
from app.pages.router import router as pages_router

app = FastAPI(
    title="ToDo"
)


@app.get("/")
def get_main():
    return "This is main page"


app.include_router(groups_router)
app.include_router(tasks_router)
app.include_router(users_router)
app.include_router(pages_router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow_Headers", "Access-Authorization"],
)

from fastapi import FastAPI
from app.groups.groups import router as groups_router

app = FastAPI(
    title="ToDo"
)


@app.get("/main")
def get_main():
    return "This is main page"


app.include_router(groups_router)

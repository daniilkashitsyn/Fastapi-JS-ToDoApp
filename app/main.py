from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.groups.groups import router as groups_router

app = FastAPI(
    title="ToDo"
)


@app.get("/", response_class=HTMLResponse)
def get_main():
    pass


app.include_router(groups_router)

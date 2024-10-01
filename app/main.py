from fastapi import FastAPI

app = FastAPI(
    title="ToDo"
)


@app.get("/main")
def get_main():
    return "This is main page"

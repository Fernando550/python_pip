import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/")
def get_inf():
    return [1,2,3]

@app.get("/inf")
def get_inf():
    return {"name": "FastAPI"}

@app.get("/home", response_class=HTMLResponse)
def get_home():
    return "<h1>Hello World</h1>"


def run():
    store.get_categories()

if __name__ == "__main__":
    run()
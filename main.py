from fastapi import FastAPI

from routers import events

from session import setup_database

setup_database()

app = FastAPI()

app.include_router(events.router)

@app.get("/")
def index():
  return { "message": "Hello, World!" }

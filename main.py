from fastapi import FastAPI

from routers import events, hosts

# from session import setup_database

# setup_database()

app = FastAPI()

app.include_router(events.router, prefix="/api")
app.include_router(hosts.router, prefix="/api")

@app.get("/")
def index():
  return { "message": "Hello, World!" }

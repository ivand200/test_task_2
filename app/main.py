# TODO: define pandentic models
# TODO: define sqlalchemy models
# TODO: insert products(20), farmers(5)
# TODO: create CRUD for models
# TODO: Add JWT Auth
# TODO: create connector

from fastapi import FastAPI, HTTPException
from .routers import app

@app.get("/")
async def home():
    return "Hello world"
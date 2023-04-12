from fastapi import FastAPI
from . import models
from .database import engine
from .routers import business_cards, users, auth

# Creating all tables in database if not exists
models.Base.metadata.create_all(bind=engine)

# Create an object FastAPI
app = FastAPI()

# Include all paths(routers)
app.include_router(business_cards.router)
app.include_router(users.router)
app.include_router(auth.router)

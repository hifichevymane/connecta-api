from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import business_cards, users, auth

# Creating all tables in database if not exists
# models.Base.metadata.create_all(bind=engine)

# Create an object FastAPI
app = FastAPI()
# Allowed origins for CORS
origins = ['*']

# Add CORS support
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Include all paths(routers)
app.include_router(business_cards.router)
app.include_router(users.router)
app.include_router(auth.router)

from fastapi import FastAPI
from src.auth.router import router as auth_router
from database import create_database_if_not_exists, Base, engine

app = FastAPI()
app.include_router(auth_router)

# Ensure DB exists
create_database_if_not_exists()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

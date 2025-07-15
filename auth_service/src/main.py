from fastapi import FastAPI
from auth_service.router import router
from database import Base, engine

app = FastAPI()

# Create DB tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(router)

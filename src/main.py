from .routers import router
from dotenv import load_dotenv
from fastapi import FastAPI
import os

load_dotenv()
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

print(MONGO_USERNAME, MONGO_PASSWORD)


app = FastAPI()

app.include_router(router)

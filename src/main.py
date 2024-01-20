from dotenv import load_dotenv
load_dotenv()

from .routers import router
from fastapi import FastAPI


app = FastAPI()

app.include_router(router)

from contextlib import asynccontextmanager

from fastapi import FastAPI

from pysatl_knowledge.api import auth, critical_value
from pysatl_knowledge.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title=settings.app_name, lifespan=lifespan)

app.include_router(auth.router)
app.include_router(critical_value.router)

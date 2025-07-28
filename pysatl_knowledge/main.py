from fastapi import FastAPI

from pysatl_knowledge.api import auth


app = FastAPI(title="PySATL-Knowledge")

app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Root endpoint working!"}

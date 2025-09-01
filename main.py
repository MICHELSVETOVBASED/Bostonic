from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, EmailStr
from items_views import router as items_router
from Users.views import router as users_router
from core.config import settings

######
from api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(items_router, prefix="/items-views")
app.include_router(users_router)
app.include_router(router=router_v1, prefix="/api/v1")


@app.get("/")
def indexing():
    return {
        "message": "Walewildering",
    }


@app.post("/calc/add")
async def add(a: int, b: int):
    return {"a": a, "b": b, "result": a + b}


@app.get("/forcen/")
def forcen(name: str = "Pleb?"):
    name = name.strip().title()
    return {
        "message": f"Hey {name}",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

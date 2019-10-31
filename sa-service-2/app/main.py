import socket
import sys

from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

hostname = socket.gethostname()

version = f"{sys.version_info.major}.{sys.version_info.minor}"


@app.get("/")
async def read_root():
    return JSONResponse(content={
        "name": "service-two",
        "host": hostname,
        "version": f"Hello world! From FastAPI running on Uvicorn with Gunicorn in Alpine. Using Python {version}"
    })

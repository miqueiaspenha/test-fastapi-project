import time

from fastapi import FastAPI
from app.routers import users

app = FastAPI(debug=True)

@app.middleware("http")
async def log_request_time(request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    print(f"{request.url.path} levou {duration:.4f} segundos")
    return response

app.include_router(users.router)
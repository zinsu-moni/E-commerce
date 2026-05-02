from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from app.api import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_cors_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.get("/")
def root():
    return {"status": "success", "message": "Insighta Labs API"}

app.include_router(router, prefix="/api")

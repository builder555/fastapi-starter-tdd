from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.module import router as module_router

origins = [
    'http://localhost',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://localhost:8080',
]

_app = FastAPI()
_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

_app.include_router(module_router, prefix='/api/v1/module', tags=['Module'])

@_app.get('/ping')
def ping():
    return {"ping": "pong!"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

# Setting middlewares
# reference: https://stackoverflow.com/questions/65635346/how-can-i-enable-cors-in-fastapi
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return {'Message': "Site is running, visit to -> localhost:8000/docs"}

# including api routes
# app.include_router(api_router, prefix=settings.API_V1_STR)


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import database, models

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])


@app.get('/')
def root():
    return {"data": "Hello world"}

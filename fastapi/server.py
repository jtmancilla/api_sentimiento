from typing import Optional
from fastapi import FastAPI, File, Query
from starlette.responses import Response
import io
from model import analize1
import logging
from pydantic import BaseModel
import json
import datetime

from helper import prepare_text
from helper import get_current_datetime


logging.basicConfig(level=logging.DEBUG)




app = FastAPI(title="Modelo NLP en Español",
              description=''' El objetivo el texto''',
              version="0.1.0",
              )


class Item(BaseModel):
    data: str


# model = analize1()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a esta API de procesamiento de texto"}


@app.post("/sentimiento/")
async def get_text(item: Item):
    ''' obtenemos el texto '''
    logging.debug("ejecutadando modelo...")

    # if item.data:
    text = prepare_text(item.data)
    result = analize1(text)
    logging.debug("modelo ejecutado...")
    
    return {
        "message": f"{result} {get_current_datetime()}"
    }
    # return {"items": "Null"}


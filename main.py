import logging
from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from model.postgres_connection import PostgresConnection
from schema.film_schema import FilmSchema
import json

app = FastAPI()
conn = PostgresConnection()

logger = logging(__name__)

@app.get("/", status_code=HTTP_200_OK)
def root():
    logger.info("logging from the root logger")
    return conn.read_all()

@app.get("/api/get/{id}", status_code=HTTP_200_OK)
def getById(id:str):
    return conn.read_one_by_id(id)

@app.post("/api/insert", status_code=HTTP_201_CREATED)
def insert(film_data:FilmSchema):
    data = film_data.dict()
    logger.info(f"successful insertion data in the DB")
    data.pop("film_id")
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)
    
@app.put("/api/update/{id}", status_code=HTTP_204_NO_CONTENT)
def update(film_data:FilmSchema, id:str):
    data = film_data.dict()
    data["film_id"] = id
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)
    
@app.delete("/api/delete/{id}", status_code=HTTP_204_NO_CONTENT)
def delete(id:str):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)
import logging
from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK
from model.postgres_connection import PostgresConnection
from schema.film_schema import FilmSchema
import json

app = FastAPI()
conn = PostgresConnection()

# logger = logging(__name__)

@app.get("/")
def root():
    # logger.info("logging from the root logger")
    return conn.read_all()

@app.get("/api/get/{id}")
def getById(id:str):
    print("Entro a la funcion")
    return conn.read_one_by_id(id)

@app.post("/api/insert")
def insert(film_data:FilmSchema):
    data = film_data.dict()
    # logger.info(f"successful insertion data in the DB")
    data.pop("film_id")
    print(film_data)
    print(data)
    conn.write(data)
    
@app.put("/api/update/{id}")
def update(film_data:FilmSchema, id:str):
    data = film_data.dict()
    data["film_id"] = id
    conn.update(data)
    
@app.delete("/api/delete/{id}")
def delete(id:str):
    conn.delete(id)
    return ("Borrado correctamete")

    
    
    
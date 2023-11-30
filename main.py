import logging
import csv
import codecs
from fastapi import FastAPI, Response, Request, File, UploadFile
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from model.postgres_connection import PostgresConnection
from schema.film_schema import FilmSchema

app = FastAPI()
conn = PostgresConnection()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('myLogger')

@app.get("/", status_code=HTTP_200_OK)
def root():
    logger.info("logging from the root logger")
    return conn.read_all()

@app.get("/api/get/{id}", status_code=HTTP_200_OK)
def getById(id:str):
    return conn.read_one_by_id(id)

@app.get("/api/get", status_code=HTTP_200_OK)
def getByGenre(genre:str):
    print("Aca entra")
    return conn.read_all_by_genre(genre)

@app.post("/api/insert", status_code=HTTP_201_CREATED)
def insert(film_data:FilmSchema):
    data = film_data.dict()
    logger.info(f"successful insertion data in the DB")
    data.pop("film_id")
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)

@app.post("api/upload/csv", status_code=HTTP_201_CREATED)
def upload_csv(file: UploadFile = File('files/mcu-movies.csv')):
    csvReader = csv.DictReader(codecs.interdecode(file.file, 'utf-8'))
    data = {}
    for rows in csvReader:
        key = rows['title']
        data[key] = rows
    file.file.close()
    return data

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
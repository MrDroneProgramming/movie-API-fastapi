from fastapi.testclient import TestClient
from fastapi import status
from main import app

client=TestClient(app=app)

def test_index_returns_all():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    
def test_index_returns_by_id():
    response = client.get('/api/get/1')
    assert response.status_code == status.HTTP_200_OK
    
def test_insert_film():
    response = client.post('/api/insert',json={"film_id":0,"title":"test","created_on":"2023-11-13T13:48:15.390Z","runtime":0,"director":"string","genre":"string"})
    assert response.status_code == status.HTTP_201_CREATED
    
def test_update_film():
    response = client.put('/api/update/3',json={"film_id":3,"title":"Iron Man Test5","created_on":"2023-11-13T13:48:15.390Z","runtime":170,"director":"Fer","genre":"CF"})
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
def test_delete_film():
    response = client.delete('/api/delete/17')
    assert response.status_code == status.HTTP_204_NO_CONTENT
# movie-api-fastapi

## Principal stack
- **Python 3.10+**
- **FastAPI 0.100.0**

## Repo Structure

## Development environment steps
1. Install Python 3.10.11
2. Crear un folder para albergar el proyecto
3. Crear un environment dentro del directorio del proyecto
    python3 -m venv nombredelenv
    py -m venv nombredelenv
4. Activar el environment
    nombredelenv\Scripts\activate.bat
5. Instalar las dependencias necesarias
    Run de requirements.txt
    pip install -r requirements.txt
2. uvicorn main:app
3. uvicorn mani:app --reload

4. Create a DB in Postgres SQL
5. Create Table:
    CREATE TABLE film (
        film_id serial PRIMARY KEY,
        title VARCHAR(50) NOT NULL,
        created_on TIMESTAMP,
        runtime INT,
        director VARCHAR(50),
        genre VARCHAR(70)
    );

# Notes:
Error psycopg solved:
    https://pypi.org/project/psycopg/
    pip install --upgrade pip           # to upgrade pip
    pip install "psycopg[binary,pool]"  # to install package and dependencies
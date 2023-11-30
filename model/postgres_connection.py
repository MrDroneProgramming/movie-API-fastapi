import psycopg

class PostgresConnection():
    conn = None
    
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=movie_api_fastapi user=postgres password=POSTGRES host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()
            
    def read_all(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                               SELECT * FROM film
                               """)
            return data.fetchall()
        
    def read_one_by_id(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                               SELECT * FROM film WHERE film_id = %s
                               """, (id,))
            return data.fetchone()
        
    def read_all_by_genre(self, genre):
        print("Aca tambien entra")
        with self.conn.cursor() as cur:
            data = cur.execute("""
                               SELECT * FROM film WHERE genre = %s
                               """, (genre,))
            return data.fetchall()
        
    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                        INSERT INTO film(title, created_on, runtime, director, genre) 
                        VALUES(%(title)s, %(created_on)s, %(runtime)s, %(director)s, %(genre)s)
                        """, data)
            self.conn.commit()
            
    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE film SET title = %(title)s, created_on = %(created_on)s, runtime = %(runtime)s, director = %(director)s, genre = %(genre)s
                WHERE film_id = %(film_id)s
                               """, data)
            self.conn.commit()
    
    def delete(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""DELETE FROM film WHERE film_id = %s
                               """, (id,)) 
            self.conn.commit()
            
    def __def__(self):
        self.conn.close()
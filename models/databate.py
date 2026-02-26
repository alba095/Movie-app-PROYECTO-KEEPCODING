import sqlite3

def init_db():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute( 
        """ CREATE TABLE IF NOT EXISTS comentario 
        ( id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pelicula TEXT,
        persona TEXT,
        comentario TEXT,
        fecha TEXT
        )
        """)
    conn.commit()
    conn.close()

def add_comment(imdbID,persona,comentario):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    from datetime import date
    fecha = date.today().isoformat()
    cursor.execute(
        "INSERT INTO comentario (id_pelicula,persona,comentario,fecha) VALUES(?,?,?,?)",
        (imdbID, persona,comentario,fecha)
    )
    conn.commit()
    conn.close()

def get_comments(id_pelicula):
    conn = sqlite3.connect("movies.db")
    conn.row_factory = sqlite3.Row #para poder acceder por el nombre
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM comentario WHERE id_pelicula = ? ",
        (id_pelicula,)
    )
    filas = cursor.fetchall()
    conn.close()
    return filas
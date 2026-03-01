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
    cursor.execute( 
        """ CREATE TABLE IF NOT EXISTS calificacion 
        ( id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pelicula TEXT,
        persona TEXT,
        calificacion INTEGER CHECK(calificacion >= 1 AND calificacion <= 5),
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

def add_calificacion(id_pelicula,persona,calificacion):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    from datetime import date
    fecha = date.today().isoformat()
    cursor.execute(
        "INSERT INTO calificacion (id_pelicula,persona,calificacion,fecha) VALUES (?,?,?,?)",
        (id_pelicula,persona,calificacion,fecha)
    )
    conn.commit()
    conn.close()
def get_rating_stats(id_pelicula):#promedio
    conn = sqlite3.connect("movies.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT AVG(calificacion) AS promedio, COUNT(*) AS total
        FROM calificacion
        WHERE id_pelicula = ?
        """,
        (id_pelicula,)
    )
    row = cursor.fetchone()
    conn.close()
    # row["promedio"] puede ser None si no hay votos
    return row["promedio"], row["total"] 
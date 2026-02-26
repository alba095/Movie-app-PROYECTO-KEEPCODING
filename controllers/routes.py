from flask import render_template, request, redirect, flash
from services.omdb_service import search_movies,get_movie_detail
from models.databate import *

def register_routes(app):

    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/buscar")
    def buscar():
        year = request.args.get("year")
        title = request.args.get("title")
        
        if not title or title.strip() == "":
            flash("El titulo es obligatorio !!!")
            return redirect("/")
        else:
            movies, error = search_movies(title, year)
            
        return render_template("results.html", year= year, title = title, movies= movies, error= error)
    
    @app.route("/movie/<imdbID>")
    def detail(imdbID):
         movie, error = get_movie_detail(imdbID)
         comment = get_comments(imdbID)
         return render_template("detail.html", movie= movie, error= error, comment = comment)
    
    @app.route("/movie/<imdbID>/comment", methods=["POST"])
    def comment(imdbID):
        persona = request.form.get("persona")
        comentario = request.form.get("comentario")
        if persona and comentario and persona.strip() and comentario.strip():
            add_comment(imdbID,persona,comentario)
            return redirect(f"/movie/{imdbID}")
        else:
            flash("Rellena todos los campos")
            return redirect(f"/movie/{imdbID}")
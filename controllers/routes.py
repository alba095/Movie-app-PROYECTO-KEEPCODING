from flask import render_template, request, redirect, flash

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
            
        return render_template("results.html", year= year, title = title)
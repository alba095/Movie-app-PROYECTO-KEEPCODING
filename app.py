from flask import Flask
from controllers.routes import register_routes
from models.databate import init_db

app = Flask(__name__)
init_db()
app.config["SECRET_KEY"] = "algo-secreto"



register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from controllers.routes import register_routes

app = Flask(__name__)
app.config["SECRET_KEY"] = "algo-secreto"


register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
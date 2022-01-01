from flask import Flask
from flask_restful import Api

from resources.facts_resource import Facts, FactsList
from db import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///veganData.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

app.secret_key = "vegan5riddhi"
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def home():
    return "~Savvy Vegan~"


api.add_resource(Facts, "/fact/<string:name>")
api.add_resource(FactsList, "/facts")


if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)

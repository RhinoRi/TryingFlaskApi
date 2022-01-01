from flask_restful import Resource, reqparse
from models.facts_model import FactsModel


class Facts(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "vName", type=str, required=True, help="This section can not be blank"
    )

    # getting the facts by name..
    def get(self, name):
        fact = FactsModel.find_by_name(name)
        if fact:
            return fact.json(), 200
        return {"message": "Fact not found."}

    # adding a new fact in the database..
    def post(self, name):
        if FactsModel.find_by_name(name):
            return {"message": "This fact already exists."}, 400

        data = Facts.parser.parse_args()
        fact = FactsModel(name, **data)
        try:
            fact.save_to_db()
        except:
            return {"message": "Error occurred."}, 500

        return fact.json(), 201

    # deleting an existing fact..
    def delete(self, name):
        fact = FactsModel.find_by_name(name)
        if fact:
            fact.delete_from_db()
            return {"message": "Fact deleted."}, 200
        return {"message": "Fact not found."}, 404

    # updating an existing fact..
    def put(self, name):
        data = Facts.parser.parse_args()

        fact = FactsModel.find_by_name(name)

        if fact:
            fact.name = data["vName"]
            fact.desc = data["vDesc"]
            fact.image = data["vImage"]
            fact.source = data["vSource"]
        else:
            fact = FactsModel(name, **data)

        fact.save_to_db()

        return fact.json(), 200


# displaying all the facts..
class FactsList(Resource):
    def get(self):
        facts = [fact.json() for fact in FactsModel.find_all()]
        return {"facts": facts}, 200

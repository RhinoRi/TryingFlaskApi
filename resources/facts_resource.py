from flask_restful import Resource, reqparse
from models.facts_model import FactsModel

from flask import Flask, jsonify, request


class Facts(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "vName", type=str, required=True, help="This section can not be blank"
    )
    parser.add_argument(
        "vDesc", type=str, required=True, help="This section can not be blank"
    )
    parser.add_argument(
        "vImage", type=str, required=True, help="This section can not be blank"
    )
    parser.add_argument(
        "vSource", type=str, required=True, help="This section can not be blank"
    )

    # getting the facts by name..
    def get(self, _id):
        fact = FactsModel.find_by_id(_id)
        if fact:
            return fact.json(), 200
        return {"message": "Fact not found."}


    # def post(self, _id):
    #     if FactsModel.find_by_id(_id):
    #         return {"message": "This fact already exists."}, 400
    #
    #     data = Facts.parser.parse_args()
    #     fact = FactsModel(_id, **data)
    #     try:
    #         fact.save_to_db()
    #     except:
    #         return {"message": "Error occurred."}, 500
    #
    #     return fact.json(), 201

    # deleting an existing fact..

    # adding a new fact in the database..
    def post(self):
        data = request.get_json()
        return jsonify({"facts": data})


    def delete(self, _id):
        fact = FactsModel.find_by_id(_id)
        if fact:
            fact.delete_from_db()
            return {"message": "Fact deleted."}, 200
        return {"message": "Fact not found."}, 404

    # updating an existing fact..
    def put(self, _id):
        data = Facts.parser.parse_args()

        fact = FactsModel.find_by_id(_id)

        if fact:
            fact.name = data["vName"]
            fact.desc = data["vDesc"]
            fact.image = data["vImage"]
            fact.source = data["vSource"]
        else:
            fact = FactsModel(_id, **data)

        fact.save_to_db()

        return fact.json(), 200


# displaying all the facts..
class FactsList(Resource):
    def get(self):
        allfacts = [fact.json() for fact in FactsModel.find_all()]
        return {"facts": allfacts}, 200

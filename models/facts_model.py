from db import db
from sqlalchemy import Column


class FactsModel(db.Model):
    __tablename__ = 'facts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    desc = db.Column(db.String(250))
    image = db.Column(db.String(100))
    source = db.Column(db.String(100))

    def __init__(self, name, desc, image, source):
        self.name = name
        self.desc = desc
        self.image = image
        self.source = source

    def json(self):
        return {
            "id": self.id,
            "vName": self.name,
            "vDesc": self.desc,
            "vImage": self.image,
            "vSource": self.source
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

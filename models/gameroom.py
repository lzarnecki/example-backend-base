from extensions import db


class GameRoomModel(db.Model):
    __tablename__ = 'gameroom'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.id
        self.name = name
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'name': self.name
        }

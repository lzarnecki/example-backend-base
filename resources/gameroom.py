from flask_restful import Resource, reqparse
from models.gameroom import GameRoomModel


class GameRoom(Resource):
    TABLE_NAME = 'gameroom'

    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True)

    def get(self, id):
        gameroom = GameRoomModel.get_by_id(id)
        if gameroom:
            return gameroom.json()
        return {'message': 'Item not found'}, 404

    def post(self, id):
        data = GameRoom.parser.parse_args()
        gameroom_model = GameRoomModel.get_by_id(id)

        gameroom_model.name = data['name']

        try:
            gameroom_model.add_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return gameroom_model.json(), 201

    def delete(self, id):
        gameroom_model = GameRoomModel.get_by_id(id)
        if gameroom_model:
            gameroom_model.delete_from_db()
            return {'message': 'Item deleted.'}

        return {'message': 'Item not found.'}, 404


class GameRoomList(Resource):
    def get(self):
        try:
            return {'gamerooms': list(map(lambda x: x.json(), GameRoomModel.query.all()))}
        except:
            return {'message': 'Item not found.'}, 404

    def post(self):
        data = GameRoom.parser.parse_args()
        gameroom_model = GameRoomModel(**data)

        try:
            gameroom_model.add_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return gameroom_model.json(), 201

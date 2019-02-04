from models.gameroom import GameRoomModel


def load_example_data(app):
    with app.app_context():
        GameRoomModel('Game Room 1').add_to_db()
        GameRoomModel('Game Room 2').add_to_db()
        GameRoomModel('Game Room 3').add_to_db()
        GameRoomModel('Game Room 4').add_to_db()
        GameRoomModel('Game Room 5').add_to_db()

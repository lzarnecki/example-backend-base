from flask import Flask, request, jsonify, render_template
from flask_restful import Api
from flask_cors import CORS

from extensions import db
from populate_db import load_example_data

from resources.gameroom import GameRoom, GameRoomList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = True

CORS(app)
api = Api(app)
db.init_app(app)

api.add_resource(GameRoom, '/api/gameroom/<int:id>')
api.add_resource(GameRoomList, '/api/gameroom')


@app.cli.command()
def create_tables():
    print("Create tables")
    db.create_all()
    load_example_data(app)


@app.route('/')
def index():
    return "Index"


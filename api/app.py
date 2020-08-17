from flask import Flask
from flask import jsonify
from db import DB
import config

app = Flask(__name__)
db = DB(
    config.REDIS['host'],
    config.REDIS['port'],
    config.REDIS['timeout'],
    config.REDIS['key_all_films']
)


@app.route('/movies', methods=['GET'])
def get_movies():
    films = db.get_all()
    return jsonify(films), 200


@app.route('/movies/<uid>', methods=['GET'])
def get_movie(uid):
    film = db.get_film(str(uid))
    return jsonify(film), 200


@app.route('/_/readiness', methods=['GET'])
def is_ready():
    return db.ping(), 200

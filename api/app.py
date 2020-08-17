from flask import Flask
from flask import jsonify
from controller import Controller
from http import HTTPStatus
import config

app = Flask(__name__)
controller = Controller(
    config.REDIS['host'],
    config.REDIS['port'],
    config.REDIS['timeout'],
    config.REDIS['key_all_films']
)


@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        films = controller.get_all()
        return jsonify(films), HTTPStatus.OK
    except ConnectionError:
        return 'INTERNAL_SERVER_ERROR', HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/movies/<uid>', methods=['GET'])
def get_movie(uid):
    try:
        film = controller.get_film(str(uid))
        return jsonify(film), HTTPStatus.OK
    except ConnectionError:
        return 'INTERNAL_SERVER_ERROR', HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/_/readiness', methods=['GET'])
def is_ready():
    try:
        controller.ping()
        return 'OK', HTTPStatus.OK
    except ConnectionError:
        return 'INTERNAL_SERVER_ERROR', HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/_/liveness', methods=['GET'])
def is_alive():
    return 'OK', HTTPStatus.OK

from flask import Flask
from flask import jsonify
from controller import Controller
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
    films, code = controller.get_all()
    return jsonify(films), code


@app.route('/movies/<uid>', methods=['GET'])
def get_movie(uid):
    film, code = controller.get_film(str(uid))
    return jsonify(film), code


@app.route('/_/readiness', methods=['GET'])
def is_ready():
    ready, code = controller.ping()
    return jsonify(ready), code


@app.route('/_/liveness', methods=['GET'])
def is_alive():
    return '', 200

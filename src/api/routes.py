"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import json
from flask import Flask, request, jsonify, url_for, Blueprint, abort
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@app.route('/api/horoscopo/<string:signo_zodiacal>', methods=['GET'])
def get_horoscopo(signo_zodiacal):
    try:
        with open('predicciones.json') as f:  # Abrimos el archivo 'predicciones.json'
            data = json.load(f)  # Cargamos el contenido del archivo en la variable 'data'

        horoscopo = data.get(signo_zodiacal)  # Obtenemos el horóscopo correspondiente al signo zodiacal

        if horoscopo is not None:  # Verificamos si existe un horóscopo para el signo zodiacal
            return jsonify(horoscopo), 200  # Devuelve el horóscopo como respuesta JSON con código 200
        else:
            abort(404)  # Envia una respuesta con código de error 404

    except Exception as e:  # Captura las excepciones que ocurra
        return jsonify({"error": str('No se pudo enviar el horoscopo')}), 500  # Devuelve un mensaje de error como respuesta JSON con código 500

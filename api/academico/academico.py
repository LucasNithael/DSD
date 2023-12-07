from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='Acadêmico', description='Exemplo de um sistema acadêmico')

ALUNO_URL = "http://127.0.0.1:8000/aluno"
MEDIA_URL = "http://127.0.0.1:5001/media"
BOLETIM_URL = "http://127.0.0.1:8000/boletim"

aluno = api.model('aluno', {
    'id': fields.Integer(),
    'nome': fields.String(),
    'matricula': fields.String(),
    'email': fields.String(),
    'disciplinas': fields.List(fields.Integer()),
})

media = api.model('media', {
    'media': fields.Float(),
    'situacao': fields.Boolean(),
})

rpg_gateway_namespace = api.namespace('academico', description='API do sistema acadêmico')

@rpg_gateway_namespace.route('/aluno/<int:id>', methods=['GET'])
class APIGatewayRolagem(Resource):
    @api.doc(params={'id': 'id do aluno'})
    @api.marshal_list_with(aluno)
    def get(self, id):
        url = f"{ALUNO_URL}/{id}"
        response = requests.get(url)
        return response.json()

@rpg_gateway_namespace.route('/media/<int:nota1>/<int:nota2>', methods=['GET'])
class APIGatewayModificador(Resource):
    @api.doc(params={'nota1': '1º Nota', 'nota2': '2º Nota'})
    @api.marshal_list_with(media)
    def get(self, nota1, nota2):
        url = f"{MEDIA_URL}/{nota1}/{nota2}"
        response = requests.get(url)
        return response.json()

if __name__ == '__main__':
    app.run(debug=True, port=5002)

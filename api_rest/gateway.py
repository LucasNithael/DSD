from flask import Flask
from flask_restx import Api, Resource, fields
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = Api(app, version='1.0', title='Gateway', description='Exemplo do uso do gateway')

resultado_modelo = api.model('gateway', {
    'img': fields.String(),
    'frase': fields.String()
})

mensagem = api.namespace('gateway')


@mensagem.route('/gera')
class mensagem_pet(Resource):
    #@api.doc(params={'id': 'busca para gerar aleatório'})
    @api.marshal_list_with(resultado_modelo)
    def get(self):
        URL_1 = "https://api.thecatapi.com/v1/images/search"
        URL_2 = "https://api.adviceslip.com/advice"
        json_1 = requests.get(URL_1).json()[0]
        json_2 = requests.get(URL_2).json().get('slip')
        img_r = json_1.get('url')
        frase = json_2.get('advice')
        return {'img': img_r, 'frase': frase}

if __name__ == '__main__':
    app.run(debug=True, port=5001)
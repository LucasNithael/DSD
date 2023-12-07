from flask import Flask
from flask_restx import Api, Resource, fields
import random

app = Flask(__name__)
api = Api(app, version='1.0', title='Media', description='Media de Aluno.')

# Defina o modelo para a resposta da API
resultado_modelo = api.model('media', {
    'media': fields.Float(description='Resultado da modificação da rolagem'),
    'situacao': fields.Boolean()
})

# Crie um namespace com um nome personalizado
rolagem_de_dado = api.namespace('media', description='Modifica a rolagem de um dado por um valor de um modificador.')


# Rota para rolar o dado
#@api.route('/rolagem_modificada/<int:rolagem>/<int:modificador>')
@rolagem_de_dado.route('/<int:nota1>/<int:nota2>')
class rolagem_modificada(Resource):
    @api.doc(params={'nota1': 'Resultado da rolagem do dado', 'nota2': 'valor do modificador'})
    @api.marshal_list_with(resultado_modelo)
    def get(self, nota1, nota2):
        """
        Modifica a rolagem de um dado por um valor de um modificador.
        parâmetro rolagem: O valor rolado no dado.
        parâmetro modificador: O número a ser adicionado como modificador.
        retorno: Valor modificado.
        """
        resultado = (float(nota1) + float(nota2))/2

        situacao = resultado >= 60    

        return {'media': resultado, 'situacao': situacao}

if __name__ == '__main__':
    app.run(debug=True, port=5001)
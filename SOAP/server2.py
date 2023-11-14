from spyne import Application, rpc, ServiceBase, Integer, Unicode, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class SistemaAcademicoService(ServiceBase):
    def __init__(self):
        self.alunos = []

    @rpc(Unicode, Float, Float, _returns=Unicode)
    def cadastrar_aluno(ctx, nome, nota1, nota2):
        aluno = {
            'nome': nome,
            'nota1': nota1,
            'nota2': nota2,
        }
        aluno['media'] = (aluno['nota1'] + aluno['nota2']) / 2
        aluno['situacao'] = ctx.calcular_situacao(aluno['media'])
        ctx.alunos.append(aluno)
        return "Aluno cadastrado com sucesso!"

    @rpc(Unicode, _returns=Unicode)
    def excluir_aluno(ctx, nome_aluno):
        for aluno in ctx.alunos:
            if aluno['nome'] == nome_aluno:
                ctx.alunos.remove(aluno)
                return "Aluno excluído com sucesso!"
        return "Aluno não encontrado."

    @rpc(_returns=Unicode)
    def listar_alunos(ctx):
        return str(ctx.alunos)

    @rpc(Float, _returns=Unicode)
    def calcular_situacao(ctx, media):
        if media >= 6:
            return 'Aprovado'
        elif media >= 4:
            return 'Recuperação'
        else:
            return 'Reprovado'

    @rpc(Unicode, _returns=Unicode)
    def exportar(ctx, arquivo):
        try:
            with open(arquivo, 'w', newline='') as file:
                write = csv.writer(file, delimiter='|')
                write.writerow(['Nome', 'Nota 1', 'Nota 2', 'Media', 'Situação'])
                for aluno in ctx.alunos:
                    write.writerow([aluno['nome'], aluno['nota1'], aluno['nota2'], aluno['media'], aluno['situacao']])
            return "Exportação para CSV realizada com sucesso!"
        except Exception as e:
            return str(e)

    @rpc(Unicode, _returns=Unicode)
    def exportar_pdf(ctx, arquivo):
        try:
            c = canvas.Canvas(arquivo, pagesize=letter)
            c.setFont("Helvetica", 12)
            c.drawString(100, 750, "RELATÓRIO DE ALUNOS".center(80, "*"))

            y = 740
            for aluno in ctx.alunos:
                y -= 15
                c.drawString(100, y, f"Nome: " + f"{aluno['nome']}".rjust(15, "."))
                y -= 15
                c.drawString(100, y, f"Nota 1: " + f"{aluno['nota1']}".rjust(15, "."))
                y -= 15
                c.drawString(100, y, f"Nota 2: " + f"{aluno['nota2']}".rjust(15, "."))
                y -= 15
                c.drawString(100, y, f"Média: " + f"{aluno['media']}".rjust(15, "."))
                y -= 15
                c.drawString(100, y, f"Situação: " + f"{aluno['situacao']}".rjust(15, "."))
                y -= 15

            c.drawString(100, y - 15, "FIM DO RELATÓRIO".center(80, "*"))

            c.save()
            return "Exportação para PDF realizada com sucesso!"
        except Exception as e:
            return str(e)

        

########## FIM DOS MÉTODOS ##########
# Criação da aplicação SOAP
application = Application([SistemaAcademicoService], 'sistema_academico',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

# Configuração do servidor WSGI
wsgi_application = WsgiApplication(application)

# Configuração do servidor HTTP
server = make_server('0.0.0.0', 8000, wsgi_application)

print("Servidor SOAP iniciado. Aguardando requisições...")
server.serve_forever()
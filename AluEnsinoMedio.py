from Aluno import Aluno

class AluEnsinoMedio (Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        Aluno.imprimir(self)
        print("Ano: " + self.ano)

    @staticmethod
    def toAluEnsinoMedio(aluno, ano):
        al_em = AluEnsinoMedio(aluno.codigo, aluno.nome, aluno.matricula, ano)
        return al_em

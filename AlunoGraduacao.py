from Aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        Aluno.imprimir(self)
        print("Semestre: " + self.semestre)

    @staticmethod
    def toAlunoGraduacao(aluno, semestre):
        al_grad = AlunoGraduacao(aluno.codigo, aluno.nome, aluno.matricula, semestre)
        return al_grad
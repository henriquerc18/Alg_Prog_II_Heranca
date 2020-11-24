# Autor: Henrique Rosa Carvalho
# Aula 08 - Herança
'''
Construa um algoritmo para implementar a classe Aluno (código, nome, matrícula).
A classe Aluno possui duas subclasses, a classe AluEnsinoMedio (ano) e AlunoGraducao(semestre).
As 3 classes possuem o método construtor o também o método construtor imprimir(), que imprime na tela
os valores de todos os atributos da sua classe.
'''

class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print("Código: " + self.codigo)
        print("Nome: " + self.nome)
        print("Matrícula: " + self.matricula)

    @staticmethod
    def toAluno(aluno):
        al = Aluno(aluno.codigo, aluno.nome, aluno.matricula)
        return al
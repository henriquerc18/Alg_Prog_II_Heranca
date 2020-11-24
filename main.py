from Aluno import Aluno
from AluEnsinoMedio import AluEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

al = Aluno("1", "Henrique", "631910184")
al_em = AluEnsinoMedio("2", "Fulano", "65651", "2020")
al_grad = AlunoGraduacao("3","Fulano2", "50555", "4")

al.imprimir()

al_em.imprimir()

al_grad.imprimir()

# 2 = mínimo 5 e máximo 6
# 0 = calouro, formando, fluxo contínuo e fluxo individual
# 1 = a remoção que atende uma troca; a remoção que atende uma inserção, a remoção, a troca e a inserção
# 2 = atender os alunos que realizou a menor quantidade de disciplinas
from calendar import c
from venv import create
from modules.subject import Subject
from modules.student import Student
from modules.subjects import *
from modules.students import *
from modules.data import *

#p1 = Subject('Programação 1', '', ['Segunda, 13:30 - 15:10', 'Quarta, 13:30 - 15:10'], 1)

#disciplinas = [p1]
#print(disciplinas[0].info())

#aluno1 = Student('Eduarda Bianca Alessandra Campos', 22050001, 1, [p1])

#alunos = [aluno1]
#print(alunos[0].info())

def createStudent():
    return

def readStudent():
    return

def updateStudent():
    return

def deleteStudent():
    return

def listAllStudent():
    return

def enrollStudent():
    return

def adjustStudent():
    return

def readjustStudent():
    return

studentOptions = [
    {'1 - Cadastrar aluno': createStudent},
    {'2 - Ver detalhes de aluno': readStudent},
    {'3 - Atualizar aluno': updateStudent},
    {'4 - Deletar aluno': deleteStudent},
    {'5 - Listar alunos': listAllStudent},
    {'6 - Matricular aluno em disciplina': enrollStudent},
    {'7 - Realizar ajuste de aluno': adjustStudent},
    {'8 - Realizar reajuste de aluno': readjustStudent},
    {'9 - Sair': exit}
]

print('SGM - Sistema de Gerenciamento de Matrículas')

while True:
    print('\nServiços disponíveis:')
    for option in studentOptions: 
        for key, value in option.items(): print(key)
    

    try:
        option = int(input('Sua opção: '))        
        list(studentOptions[option-1].values())[0]()

    except Exception:
        print('\nOpção inválida')



#print(disciplinas)
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

def searchStudent(reg):
    if int(reg) > len(alunos) + 1:
        print('Matrícula inválida')
        return
    
    student = None        
    for student1 in alunos:
        if reg == student1.getInfo()['registration']:
            student = student1

    if student == None:
        print('Aluno não encontrado')
    
    return student

def createStudent():
    print('\n--- Cadastrar novo aluno no sistema ---')

    name = input('Nome do estudante: ')
    reg = f"{len(alunos)+1:08}"
    period = 1
    enrolledSubjects = []
    Student(name, reg, period, enrolledSubjects)

    print(f'Novo aluno com matrícula {reg} cadastrado')
    return

def readStudent():
    print('\n--- Ver detalhes do aluno ---')
    reg = input('Matrícula do estudante: ')
    
    student = searchStudent(reg)
    if student != None: print(student.getInfo())
    
    return

def updateStudent():
    print('\n--- Atualizar dados do aluno ---')
    reg = input('Matrícula do estudante: ')

    student = searchStudent(reg)
    if student != None: print(student.getInfo())
    
    return

def deleteStudent():
    print('\n--- Deletar aluno do sistema ---')
    reg = input('Matrícula do estudante: ')

    student = searchStudent(reg)
    if student != None:
        alunos.remove(student)
        print('Aluno deletado')

    return

def listAllStudent():
    print('\n--- Listar todos os alunos ---')
    for x in range(len(alunos)):
        aluno = alunos[x]
        print(f'{x} - {aluno.getInfo()}\n')

    return

def enrollStudent():
    print('\n--- Matricular aluno em disciplina ---')
    reg = input('Matrícula do estudante: ')

    return

def adjustStudent():
    print('\n--- Ajuste de aluno ---')
    reg = input('Matrícula do estudante: ')

    return

def readjustStudent():
    print('--- Reajuste de aluno ---')
    reg = input('Matrícula do estudante: ')

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

    option = int(input('Sua opção: '))        
    list(studentOptions[option-1].values())[0]()
    #try:
        #option = int(input('Sua opção: '))        
        #list(studentOptions[option-1].values())[0]()

    #except Exception:
    #    print('\nOpção inválida')

#print(disciplinas)
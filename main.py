# matricula, ajuste e reajuste
# 2 = mínimo 5 e máximo 6
# 0 = calouro, formando, fluxo contínuo e fluxo individual
# 1 = a remoção que atende uma troca; a remoção que atende uma inserção, a remoção, a troca e a inserção
# 2 = atender os alunos que realizou a menor quantidade de disciplinas
from calendar import c
from venv import create
from modules.subject import Subject
from modules.student import Student
from modules.subjects import *
#from modules.students import *
from modules.data import *

#p1 = Subject('Programação 1', '', ['Segunda, 13:30 - 15:10', 'Quarta, 13:30 - 15:10'], 1)
\
#disciplinas = [p1]
#print(disciplinas[0].info())

#aluno1 = Student('Eduarda Bianca Alessandra Campos', 22050001, 1, [p1])

#alunos = [aluno1]
#print(alunos[0].info())

minDisc = 5
maxDisc = 6
studentPriority = ['Calouro', 'Formando', 'Fluxo contínuo', 'Fluxo individual']
queue = []

# [0, 1, 1, 2, 2, 0]

def addToQueue(studentType, action):
    # sort queue by priority    
    priority = studentPriority.index(studentType)
    queue.append((priority, action)) #ação adicionada ao fim da fila    
    # loop para fazer a permuta das ações com base na prioridade
    # percorrendo a fila de trás pra frente pra encontrar
    # o próximo valor de prioridade igual ou menor ao atual
    # para adicionar na posição à frente deste
    for i in range(2, len(queue)-1):
        topic = queue[-i]
        lastAdded = queue[-1]
        
        if topic[0] <= lastAdded[0]:
            # dividindo o array em dois para fazer a permuta de elementos
            index = len(queue)-i+1
            queueAhead = queue[index: -1]
            queue = queue[:index]
            # adicionando a função na sua respectiva posição de prioridade
            queue.append(lastAdded)
            # juntando os dois arrays novamente
            queue = queue+queueAhead
            
            # fazendo backup do elemento adiante ao
            # que será permutado
            


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


def searchSubject(cod):
    if int(cod) > len(disciplinas) + 1:
        print('Disciplina inválida')
        return
    
    subject = None        
    for subject1 in disciplinas:
        if cod == subject1.getInfo()['cod']:
            subject = subject1

    if subject == None:
        print('Disciplina não encontrada')
    
    return subject


# subject methods
def enroll(regStudent, codSubject):       
    student = searchStudent(regStudent)
    subject = searchSubject(codSubject)

    for subRequirements in subject.requirements:
        if subRequirements not in student.finishedSubjects:
            print('Aluno não tem o(s) pré-requisito(s) necessário(s) para cursar a disciplina')
            return
    
    studentStatus = student.getInfo()['status']
    studentFlow = student.getInfo()['flow']

    studentType = studentStatus if studentStatus != '' else studentFlow
    addToQueue(studentType, student.enrolledSubjects.append(subject))
    
    return


def readSubjects():
    print('\n--- Listar todas as disciplinas ---')
    for x in range(len(disciplinas)):
        subject = disciplinas[x]
        print(f'{x+1} - {subject.getInfo()}\n')

    return 


def adjust(student, subject, method, reason):
    return 


# student methods
def createStudent():
    print('\n--- Cadastrar novo aluno no sistema ---')

    name = input('Nome do estudante: ')
    reg = f"{len(alunos)+1:08}"
    period = 1
    enrolledSubjects = []
    finishedSubjects = []
    Student(name, reg, period, enrolledSubjects, finishedSubjects)

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
        print(f'{x+1} - {aluno.getInfo()}\n')

    return


def enrollStudent():
    print('\n--- Matricular aluno em disciplina ---')
    reg = input('Matrícula do estudante: ')
    codDisc = input('Código da disciplina: ')
    
    enroll(reg, codDisc)
    return


def adjustStudent():
    print('\n--- Ajuste de aluno ---')
    reg = input('Matrícula do estudante: ')

    return


def readjustStudent():
    print('--- Reajuste de aluno ---')
    reg = input('Matrícula do estudante: ')

    return


def applyOp():
    return

print('SGM - Sistema de Gerenciamento de Matrículas')

studentOptions = [
    {'1 - Cadastrar aluno': createStudent},
    {'2 - Ver detalhes de aluno': readStudent},
    {'3 - Atualizar aluno': updateStudent},
    {'4 - Deletar aluno': deleteStudent},
    {'5 - Listar alunos': listAllStudent},
    {'6 - Matricular aluno em disciplina': enrollStudent},
    {'7 - Realizar ajuste de aluno': adjustStudent},
    {'8 - Realizar reajuste de aluno': readjustStudent},
    {'9 - Listar disciplinas': readSubjects},
    {'10 - Aplicar ações': applyOp},
    {'11 - Sair': exit}
]


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
# 2 = mínimo 5 e máximo 6
# 0 = calouro, formando, fluxo contínuo e fluxo individual
# 1 = a remoção que atende uma troca; a remoção que atende uma inserção, a remoção, a troca e a inserção
# 2 = atender os alunos que realizou a menor quantidade de disciplinas
from modules.subject import Subject
from modules.student import Student

p1 = Subject('Programação 1', '', ['Segunda, 13:30 - 15:10', 'Quarta, 13:30 - 15:10'], 1)

disciplinas = [p1]
print(disciplinas[0].info())

aluno1 = Student('Eduarda Bianca Alessandra Campos', 22050001, 1, [p1])

alunos = [aluno1]
print(alunos[0].info())

from ast import Sub
from tkinter import W
from modules.subject import Subject
from modules.data import *


    #Primeiro Periodo
p1 = Subject('Programação 1', [], ['Segunda, 13:30 - 15:10', 'Quarta, 13:30 - 15:10'], 1)
cse = Subject('Computação Sociedade e Ética', [], ['Segunda, 15:20 - 17:00', 'Quarta, 13:30 - 17:00'], 1)
logica = Subject('Lógica de Computação', [], ['Terça, 13:30 - 15:10', 'Quinta, 13:30 - 15:10'], 1)
md = Subject('Matemática Discreta', [], ['Terça, 15:20 - 17:00', 'Quinta, 15:20 - 17:00'], 1)
cdi = Subject('Cálculo Diferencial e Integral', [], ['Sexta, 13:30 - 17:00'], 1)

    #Segundo periodo
estdd = Subject("Estrutura de Dados", [p1.getInfo()], ['Segunda, 13:00 - 15:10', 'Quarta, 13:00 - 15:20'], 2)
bd = Subject("Banco de Dados", [], ['Segunda, 15:20 - 17:00', 'Quarta, 15:20 - 17:00'], 2)
oac = Subject("Organização e Arquitetura de Computadores", [], ['Terça, 13:00 - 15:10', 'Quinta, 13:00 - 15:10'], 2)
ga = Subject("Geometria Analítica", [], ['Terça - 15:20 - 17:00', 'Quinta, 15:20 - 17:00'], 2)

    #Terceiro periodo
redes = Subject('Redes de Computadores', [], ['Segunda, 13:30 - 15:10', 'Quarta, 13:30 - 15:10'], 3)
grafos = Subject('Teoria dos Grafos', [], ['Segunda, 15:20 - 17:00', 'Quinta, 15:20 - 17:00'], 3)
pe = Subject('Probabilidade e estatistica', [cdi.getInfo()], ['Terça, 13:30 - 15:10', 'Quinta, 13:30 - 15:10'], 3)
al = Subject('Álgebra Linear', [ga.getInfo()], ['Terça, 15:20 - 17:00', 'Quinta, 15:20 - 17:00'], 3)

    #Quarto periodo
p2 = Subject("Programação 2", [estdd.getInfo(), bd.getInfo(), redes.getInfo()], ['Segunda, 13:00 - 15:10', 'Quarta, 13:00 - 15:20'], 4)
p3 = Subject("Programação 3", [estdd.getInfo(), bd.getInfo(), redes.getInfo()], ['Segunda, 15:20 - 17:00', 'Quarta, 15:20 - 17:00'], 4)
paa = Subject("Projeto e Análise de Algoritmos", [estdd.getInfo(), grafos.getInfo()], ['Terça, 13:00 - 15:10', 'Quinta, 13:00 - 15:10'], 4)
tc = Subject("Teoria da Computação", [], ['Terça - 15:20 - 17:00', 'Quinta, 15:20 - 17:00'], 4)

    #Quinto Periodo
sistemas = Subject('Sistemas Operacionais', [oac.getInfo()], ['Segunda, 13:30 - 15:10', 'Quarta, 13:30 - 15:10'], 5)
compiladores = Subject('compiladores', [estdd.getInfo(), tc.getInfo()], ['Segunda, 15:20 - 17:00', 'Quarta, 15:20 - 17:00'], 5)
ia = Subject('Inteligência Artificial', [logica.getInfo(), estdd.getInfo()], ['Terça, 13:30 - 15:10', 'Quinta, 13:30 - 15:10'], 5)
cg = Subject('Computação Gráfica', [], ['Terça, 15:20 - 17:00', 'Quinta, 15:20 - 17:00'], 5)

    #Sexto periodo = Projeto
pds = Subject('Projeto e Desenvolvimento de Sistemas', [subject for subject in disciplinas if subject['availableAt'] <= 5], ['Segunda 13:00 - 17:00', 'Quarta, 13:00 - 17:00'], 6)

#Setimo Periodo
mpti = Subject('Metodologia de Pesquisa e Trabalho Individual', [], ['Segunda, 13:30 - 15:10', 'Quarta, 13:30 - 15:10'], 7)
nocoes = Subject('Noções de Direito', [], ['Segunda, 15:20 - 17:00', 'Quarta, 15:20 - 17:00'], 7)


#Eletivas
c3 = Subject('Cálculo 3', [cdi.getInfo()], ['Terça, 13:30 - 15:10', 'Quinta, 13:30 - 15:10'], 2)
clp = Subject('Conceitos de Linguagem de Programação', [], ['Segunda, 07:30 - 09:10', 'Quarta, 07:30 - 09:10'], None)
am = Subject('Aprendizagem de Máquina', [c3.getInfo()], ['Segunda, 09:20 - 12:10', 'Quarta, 09:20 - 12:10'], None)
sd = Subject('Sistemas Distribuídos', [], ['Segunda, 15:20 - 17:00', 'Quarta, 15:20 - 17:00'], None)
rnap = Subject('Redes Neurais e Aprendizado Profundo', [], ['Terça, 15:20 - 17:00', 'Quinta, 15:20 - 17:00'], None)
ihm = Subject('Interação Homem-Máquina', [p3.getInfo()], ['Sexta, 07:30 - 11:30'], None)
pdi = Subject('Processamento Digital de Imagens', [cg.getInfo()], ['Terça, 13:30 - 15:10', 'Quinta, 13:30 - 15:10'], 6)
compEv = Subject('Redes Neurais e Aprendizado Profundo', [], ['Segunda, 15:20 - 17:00', 'Quarta, 15:20 - 17:00'], None)

sisEm = Subject('Sistemas Embarcados', [], ['Terça, 13:30 - 15:10', 'Quinta, 13:30 - 15:10'], 2)
gep = Subject('Gerência de Projeto', [pds.getInfo()], ['Segunda, 13:30 - 15:10', 'Quarta, 13:30 - 15:10'], 7)
vc = Subject('Visão Computacional', [], ['Terça, 15:20 - 17:10', 'Quinta, 15:20 - 17:10'], 2)
cd = Subject('Ciência de Dados', [pe.getInfo()], ['Segunda, 07:30 - 09:10', 'Quarta, 07:30 - 09:10'], 4)
micap = Subject('Microcontroladores e Aplicações', [], ['Segunda, 15:20 - 17:00', 'Quarta, 15:20 - 17:00'], None)
ssc = Subject('Segurança de Sistemas Computacionais', [redes.getInfo()], ['Segunda, 13:30 - 15:10', 'Quarta, 13:30 - 15:10'], None)

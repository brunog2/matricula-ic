from contextlib import redirect_stderr
from modules.student import Student
from modules.data import *
from modules.subjects import *

# colocar as disciplinas criadas em subjects.py dentro do array (último atributo)
aluno1 = Student('Vicente Raimundo Anthony da Rosa', '00000001', 1, [p1.getInfo(), cse.getInfo(), logica.getInfo(), md.getInfo(), cdi.getInfo()])

aluno2 = Student('Matheus Felipe de Melo Ferreira', '00000002', 1, [p1.getInfo(), cse.getInfo(), logica.getInfo(), md.getInfo(), cdi.getInfo()])

aluno3 = Student('Matheus Augusto do Santos Miranda', '00000003', 2, [estdd.getInfo(), bd.getInfo(), oac.getInfo(), ga.getInfo()])

aluno4 = Student('Thassia Maria Bittencourt', '00000004', 2, [estdd.getInfo(), bd.getInfo(), oac.getInfo(), ga.getInfo()])

aluno5 = Student('João Alves da Silva', '00000005', 3, [redes.getInfo(), grafos.getInfo(), pe.getInfo(), al.getInfo()])

aluno6 = Student('Marcos Mion Campos', '00000006', 3, [redes.getInfo(), grafos.getInfo(), pe.getInfo(), al.getInfo()])

aluno7 = Student('Vinicius Siqueira Rosalvo', '00000007', 4, [p2.getInfo(), p3.getInfo(), paa.getInfo(), tc.getInfo()])

aluno8 = Student('Levy Anthony Safadi Melo', '00000008', 4, [p2.getInfo(), p3.getInfo(), paa.getInfo(), tc.getInfo()])

aluno9 = Student('Maria Amanda de Andrade', '00000009', 5, [sistemas.getInfo(), compiladores.getInfo(), tc.getInfo(), cg.getInfo(), ia.getInfo()])

aluno10 = Student('Manuela de Andrade Bezerra', '00000010', 5, [sistemas.getInfo(), compiladores.getInfo(), tc.getInfo(), cg.getInfo(), ia.getInfo()])

aluno11 = Student('Jonn Cavalcante Negrini', '000000011', 6, [pds.getInfo()])

aluno11 = Student('Alexandre Costa Alves', '00000012', 6, [pds.getInfo()])

aluno12 = Student('Larissa Fontan de Melo', '00000013', 7, [mpti.getInfo(), nocoes.getInfo()])

aluno13 = Student('Lays Kunzler Lemos', '00000014', 7, [mpti.getInfo(), nocoes.getInfo()])

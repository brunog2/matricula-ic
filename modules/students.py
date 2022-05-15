from contextlib import redirect_stderr
from modules.student import Student
from modules.data import *
from modules.subjects import *

# colocar as disciplinas criadas em subjects.py dentro do array (último atributo)
aluno1 = Student('Vicente Raimundo Anthony da Rosa', '79517258', 1, [p1.getInfo(), cse.getInfo(), logica.getInfo(), md.getInfo(), cdi.getInfo()])

aluno2 = Student('Matheus Felipe de Melo Ferreira', '25293645', 1, [p1.getInfo(), cse.getInfo(), logica.getInfo(), md.getInfo(), cdi.getInfo()])

aluno3 = Student('Matheus Augusto do Santos Miranda', '20212219', 2, [estdd.getIngo(), bd.getInfo(), oac.getInfo(), ga.getInfo()])

aluno4 = Student('Thassia Maria Bittencourt', '36947586', 2, [estdd.getIngo(), bd.getInfo(), oac.getInfo(), ga.getInfo()])

aluno5 = Student('João Alves da Silva', '93949582', 3, [redes.getInfo(), grafos.getInfo(), pe.getInfo(), al.getInfo()])

aluno6 = Student('Marcos Mion Campos', '47748221', 3, [redes.getInfo(), grafos.getInfo(), pe.getInfo(), al.getInfo()])

aluno7 = Student('Vinicius Siqueira Rosalvo', '12344321', 4, [p2.getInfo(), p3.getInfo(), paa.getInfo(), tc.getInfo()])

aluno8 = Student('Levy Anthony Safadi Melo', '65896971', 4, [p2.getInfo(), p3.getInfo(), paa.getInfo(), tc.getInfo()])

aluno9 = Student('Maria Amanda de Andrade', '75049832', 5, [sistemas.getInfo(), compiladores.getInfo(), tc.getInfo(), cg.getInfo(), ia.getInfo()])

aluno10 = Student('Manuela de Andrade Bezerra', '95798124', 5, [sistemas.getInfo(), compiladores.getInfo(), tc.getInfo(), cg.getInfo(), ia.getInfo()])

aluno11 = Student('Jonn Cavalcante Negrini', '96287582', 6, [pds.getInfo()])

aluno11 = Student('Alexandre Costa Alves', '82756249', 6, [pds.getInfo()])

aluno12 = Student('Larissa Fontan de Melo', '91926564', 7, [mpti.getInfo(), nocoes.getInfo()])

aluno13 = Student('Lays Kunzler Lemos', '25792111', 7, [mpti.getInfo(), nocoes.getInfo()])

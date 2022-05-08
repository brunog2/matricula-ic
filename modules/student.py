from modules.data import *

class Student:
    def __init__(self, name, registration, period, enrolledSubjects):
        self.name = name
        self.registration = registration
        self.period = period
        self.enrolledSubjects = enrolledSubjects        
        self.status = 'Calouro' if self.period == 1 else 'Formando' if self.period == 8 else ''
        
        if all(subject['availableAt'] == self.period for subject in self.enrolledSubjects): self.flow = 'Fluxo Padrão'
        else: self.flow = 'Fluxo Individual'

        alunos.append(self.getInfo())

    def getInfo(self):
        subjects = [subject for subject in self.enrolledSubjects]
        info = {
            'name': self.name,
            'registration': self.registration,
            'period': self.period,
            'enrolledSubjects': subjects,
            'status': self.status,
            'flow': self.flow
            }

        return info

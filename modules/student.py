class Student:
    def __init__(self, name, registration, period, enrolledSubjects):
        self.name = name
        self.registration = registration
        self.period = period
        self.enrolledSubjects = enrolledSubjects

    def info(self):
        subjects = [subject.info() for subject in self.enrolledSubjects]
        output = {'Nome': self.name, 'Matrícula': self.registration, 'Período': self.period, 'Disciplinas matriculadas': subjects}
        return output

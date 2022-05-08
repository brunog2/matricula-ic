class Student:
    def init(self, name, registration, period, enrolledSubjects, status):
        self.name = name
        self.registration = registration
        self.period = period
        self.enrolledSubjects = enrolledSubjects
        self.status = status


    def info(self):
        if self.period == 1:
            self.status = 'calouro'
        elif self.period >= 6:
            self.status = 'formando'
        elif self.period:
            pass

        subjects = [subject.info() for subject in self.enrolledSubjects]
        output = {'Nome': self.name, 'Matrícula': self.registration, 'Período': self.period, 'Disciplinas matriculadas': subjects, 'Status': self.status}
        return output

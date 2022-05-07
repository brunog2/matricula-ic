class Subject:
    def __init__(self, name, requirements, schedule, availableAt):
        self.name = name
        self.requirements = requirements
        self.schedule = schedule
        self.availableAt = availableAt

    def info(self):
        output = {
            'Nome': self.name,
            'Requisitos': self.requirements,
            'Horário': self.schedule,
            'Disponível em (período)': self.availableAt
        }
        return output

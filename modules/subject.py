from modules.data import *

class Subject:
    def __init__(self, name, requirements, schedule, availableAt):
        self.name = name
        self.requirements = requirements
        self.schedule = schedule
        self.availableAt = availableAt
        disciplinas.append(self.getInfo())

    def getInfo(self):
        info = {
            'name': self.name,
            'requirements': self.requirements,
            'schedule': self.schedule,
            'availableAt': self.availableAt
        }
        
        return info
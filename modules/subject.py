from modules.data import *

class Subject:
    def __init__(self, name, requirements, schedule, availableAt):
        self.cod = f"{len(disciplinas)+1:08}"
        self.name = name
        self.requirements = requirements
        self.schedule = schedule
        self.availableAt = availableAt
        disciplinas.append(self)

    def getInfo(self):
        requirements = [sub.getInfo() for sub in self.requirements]
        info = {
            'cod': self.cod,
            'name': self.name,
            'requirements': requirements,
            'schedule': self.schedule,
            'availableAt': self.availableAt
        }
        
        return info
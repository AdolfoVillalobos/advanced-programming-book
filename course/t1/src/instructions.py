from abc import ABC, abstractmethod
from buildings import DCCowork, Walls, Barracks
from person import Soldier, Worker, Assistant

class Instruction(ABC):
    num = 0
    def __init__(self):
        self.executed = False

    @property
    @abstractmethod
    def message(self):
        pass

    @abstractmethod        
    def action(self, **input):
        pass

    @abstractmethod
    def write_action(self):
        pass

    def __repr__(self):
        return self.message

class CreatePerson(Instruction):
    def __init__(self):
        pass

    def action(self, person_type):
        if person_type == "soldado":
            return Soldier()
        elif person_type == "trabajador":
            return Worker()
        elif person_type == "ayudante":
            return Assistant()

class AttackCivilization(Instruction):
    def __init__(self):
        pass

    def action(self, c1, c2):
        pass

class Build(Instruction):
    def __init__(self):
        pass

    def action(self, building_type):
        if building_type == "cuartel":
            return Barracks()
        elif building_type == "muralla":
            return Walls()
        elif building_type == "dccowork":
            return DCCowork()

class CollectResource(Instruction):
    def __init__(self):
        pass

    def action(self, resource_type, amount):
        return amount




from abc import ABC, abstractmethod
from src.buildings import DCCowork, Walls, Barracks
from src.person import Soldier, Worker, Assistant

class Action(ABC):
    num = 0
    def __init__(self, player_id, turns_to_completion):
        self.turns_left = turns_to_completion
        self.__player_id = player_id
    
    @property
    def player_id(self):
        return self.__player_id

    @property
    def turns_left(self):
        return self.__turns_left

    @property
    def is_due(self):
        return self.turns_left <= 0

    @turns_left.setter
    def turns_left(self, value):
        if value > 0:
            self.__turns_left = value
        else:
            self.__turns_left = 0

    @abstractmethod        
    def action(self, **input):
        pass

    def tick(self):
        self.turns_left = self.turns_left - 1

    def __repr__(self):
        out = ""
        out += f"Action: {self.__class__.__name__}\n"
        out += f"\tTurns Left: {self.turns_left}\n"
        return out


class CreatePerson(Action):
    def __init__(self, person_type, person_quantity, **kwargs):
        super().__init.__(turns_to_completion=1, **kwargs)
        self.person_type = person_type
        self.person_quantity = person_quantity

    def action(self):
        pass

class AttackCivilization(Action):
    def __init__(self, opponent_id, **kwargs):
        super().__init.__(turns_to_completion=1, **kwargs)
        self.opponent_id = opponent_id

    def action(self):
        pass

class CreateBuilding(Action):
    def __init__(self, building_type, **kwargs):
        super().__init__(**kwargs)
        self.building_type = building_type

    def action(self):
        pass

class CollectResource(Action):
    def __init__(self, resource_type, num_workers, **kwargs):
        super().__init__(turns_to_completion=1, **kwargs)
        self.resource_type = resource_type
        self.num_workers = num_workers

    def action(self):
        pass




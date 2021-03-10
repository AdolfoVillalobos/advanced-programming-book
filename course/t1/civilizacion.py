from abc import ABC, abstractmethod
import random
from buildings import UrbanCenter, Barracks, Walls

class Civilization(ABC):
    def __init__(self, person_limit, pa=0, fs=0, c_tech=0, c_stone=0, c_gold, c_wood):
        self.person_limit =  person_limit

        self.__soldiers = []
        self.__workers = []
        self.__assistants = []
        self.__walls = []
        self.__barracks = None
        self.__urban_center = UrbanCenter()
        
        # Resource points
        self.__c_tech = c_tech
        self.__c_gold = c_gold
        self.__c_wood = c_wood
        self.__c_stone = c_stone
    
    @property
    @abstractmethod
    def leader(self):
        pass

    # Person properties

    @property
    def soldiers(self):
        self.__soldiers.sort(key=lambda s: s.hp, reverse=True)
        return self.__soldiers
    
    @property
    def walls(self):
        self.__walls.sort(key=lambda s: s.hp, reverse=True)
        return self.__walls
    
    @property
    def workers(self):
        self.__workers.sort(key=lambda s: s.hp, reverse=True)
        return self.__workers

    @property
    def barracks(self):
        return self.__barracks

    @property
    def urban_center(self):
        return [self.__urban_center]
    
    @property
    def num_assistants(self):
        return len(self.__assistants)
    
    @property
    def num_workers(self):
        return len(self.__workers)

    @property
    def num_soldiers(self):
        return len(self.__soldiers)

    # Resource Properties
    @property
    def gold(self):
        return self.__c_gold

    @property
    def wood(self):
        return self.__c_wood

    @property
    def stone(self):
        return self.__c_stone

    @property
    def tech(self):
        return self.__c_tech

    @gold.setter
    def gold(self, value):
        self.__c_gold = value
 
    @wood.setter
    def wood(self, value):
        self.__c_wood = value
 
    @stone.setter
    def stone(self, value):
        self.__c_stone = value
    
    @tech.setter
    def tech(self, value):
        self.__c_tech = value

    # Attack and Defense Properties

    @property
    def HPS(self):
        return sum([soldier.hp for soldier in self.soldiers if soldier.defending])
    
    @property
    def HPT(self):
        return sum([worker.hp for worker in self.workers])

    @property
    def HPE(self):
        wall_hp = sum([wall.hp for wall in self.walls])
        urban_center_hp = self.__urban_center.hp
        barrack_hp = 0
        if self.__barracks:
            barrack_hp += self.__barracks.hp
        return wall_hp+urban_center_hp+barrack_hp

    @property
    def BD(self):
        return self.HPS+self.HPT+self.HPE

    @property
    def FS(self):
        return sum([soldier.pa for soldier in self.soldiers])

    @property
    @abstractmethod
    def PA(self):
        pass

    @property
    @abstractmethod
    def PD(self):
        pass

    # Properties research
    @property
    def IQ(self):
        return sum([a.iq for a in self.__assistants])
    
    @property
    def PT(self):
        return self.IQ/100

    # Action Methods

    @property
    def alive(self):
        return self.__urban_center.hp > 0

    def attack_other_civilization(self, other):
        if self.PA >= other.PD:
            # Gain resources
            self.__c_gold += random.randint(0, other.gold)
            self.__c_wood += random.randint(0, other.wood)
            self.__c_stone += random.randint(0, other.stone)
            self.assistants.extend(random.sample(other.assistants, random.randint(0, other.num_assistants)))
        else:
            other.defend_attack(self)

    def defend_attack(self, other):
        attack = other.PA
        for defense_line in [self.walls, self.soldiers, self.workers, self.urban_center]:
            while defense_line and (attack > 0):
                d = defense_line[-1]
                if attack >= d.hp:
                    attack -= d.hp
                    defense_line.pop()
                else:
                    defense_line[-1] -= attack
                    attack = 0

    def investigation(self):
        self.__c_tech += self.PT

    def __repr__(self):
        ret = ""
        ret += "Gold: {} -> Wood :{} -> Stone: {} \n".format(self.gold, self.wood, self.stone)
        ret += "Workers: {} -> Soldiers: {} -> Assistants: {}\n".format(self.num_workers, self.num_soldiers, self.num_assistants)
    
    

class DCC(Civilization):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def leader(self):
        return "Doctor Valdivieso"
    
    @property
    def PA(self):
        return self.FS+self.tech

    @property
    def PD(self):
        return self.BD+100*len(self.assistants)

class LaComarca(Civilization):

    def __init__(self,  **kwargs):
        super().__init__(**kwargs)

    @property
    def leader(self):
        return "Gran Polea"
    
    @property
    def PA(self):
        return round(self.FS+self.stone/2)
    
    def PD(self):
        return round(self.BD+self.wood/2)

class Cobreloa(Civilization):
    
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)

    @property
    def leader(self):
        return "Cruz"

    @property
    def PA(self):
        return round(self.FS*1.15)

    @property
    def PD(self):
        return round(self.BD*1.1)
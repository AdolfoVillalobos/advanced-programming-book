import random
from data.constantes import MAX_ATAQUE_SOLDADO, MAX_CANTIDAD_RECURSO, MAX_HP_PERSONA, MAX_IQ_AYUDANTE, MIN_ATAQUE_SOLDADO, MIN_CANTIDAD_RECURSO, MIN_HP_PERSONA, MIN_IQ_AYUDANTE

class Person:
    def __init__(self):
        self._hp = random.randint(MIN_HP_PERSONA, MAX_HP_PERSONA)
        self._available = True

    @property
    def hp(self):
        return self._hp

    @property
    def available(self):
        return self._available
    
    @hp.setter
    def hp(self, value):
        self._hp = value

    @available.setter
    def available(self, value):
        self._available = value



class Worker(Person):
    def __init__(self):
        super().__init__()

    def get_resource(self, resource_type):
        quantity = random.randint(MIN_CANTIDAD_RECURSO, MAX_CANTIDAD_RECURSO)
        return quantity

class Assistant(Person):
    def __init__(self):
        super().__init__()
        self._iq = random.randint(MIN_IQ_AYUDANTE, MAX_IQ_AYUDANTE) 
    
    @property
    def iq(self):
        return self._iq

class Soldier(Person):
    def __init__(self):
        super().__init__()
        self._power_attack = random.randint(MIN_ATAQUE_SOLDADO, MAX_ATAQUE_SOLDADO)
        self.__defending = True

    @property
    def pa(self):
        return self._power_attack

    @property
    def defending(self):
        return self.__defending
    
    @defending.setter
    def defending(self, value):
        self.__defending = value
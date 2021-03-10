from person import Worker, Assistant, Soldier

class Building:
    def __int__(self, initial_health_points,
                c_gold, c_wood, c_stone, c_workers, c_time,
                p_gold, p_wood, p_stone):

        self.__hp = initial_health_points

        # Construction requirements for resources, workers and turns
        self.__c_gold = c_gold
        self.__c_wood = c_wood
        self.__c_stone = c_stone
        self.__c_workers = c_workers
        self.__c_time = c_time

        # Usage requirements
        self.__p_gold = p_gold
        self.__p_wood = p_wood
        self.__p_stone = p_stone

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value
    
    def create_person(self):
        return "This building can't create persons"

class UrbanCenter(Building):
    def __init__(self):
        super().__init__()

    def create_person(self):
        w = Worker() 
        return w

    def destruction(self):
        pass

class Barracks(Building):
    def __init__(self):
        super().__init__()

    def create_person(self):
        p = Soldier()
        return p

class DCCowork(Building):
    def __init__(self):
        super().__init__()

    def create_person(self):
        a = Assistant()
        return a

class Walls(Building):
    def __init__(self):
        super().__init__()

    def create_person(self):
        return super().create_person()
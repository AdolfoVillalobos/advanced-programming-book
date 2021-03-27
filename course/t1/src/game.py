
from src.civilizacion import Civilization, Cobreloa, DCC, LaComarca
from src.menu import Menu


class Game:

    def __init__(self):
        print("Welcome to DCCivilization!\n")
        self.game_on = True
        self.stage = 0
        self.menu = Menu()

        self.opponents = []

    # Properties
    @property
    def player(self):
        return self.__player

    @property
    def opponents(self):
        return self.__opponents
    
    @property
    def game_on(self):
        return self.__game_on

    @property
    def stage(self):
        return self.__stage

    # Setters
    
    @player.setter
    def player(self, value):
        if not isinstance(value, Civilization): raise Exception("Player must be instance of Civilization")
        self.__player = value

    @stage.setter
    def stage(self, value):
        self.__stage = value
    
    @game_on.setter
    def game_on(self, value):
        self.__game_on = value
    
    @opponents.setter
    def opponents(self, value):
        self.__opponents = value


    # Game Methods

    def play(self):

        while True:

            self.menu.show_options()
            self.menu.get_user_input()
            current_input = self.menu.user_input

            if self.stage == 0:
                if current_input == 1:
                    self.stage = 1
                    self.menu.stage = 1 
                elif current_input == 2:
                    self.stage = -1
                    self.menu.stage = -1

            elif self.stage == 1:
                self.initialize_player(current_input)
                self.initialize_opponents(current_input)
                self.stage = 2
                self.menu.stage=2
    

    def initialize_player(self, user_input):
        civ_name = self.menu.menu_options[user_input]
        civ = self.create_civilization(civ_name, id=0)
        self.player = civ

    def initialize_opponents(self, user_input):
        opponent_names = [name for key, name in self.menu.menu_options.items() if key != user_input]
        for i, opponent in enumerate(opponent_names):
            civ = self.create_civilization(opponent, id=i+1)
            self.__opponents.append(civ)


    def create_civilization(self, name, **kwargs):
        if name == "DCC":
            return DCC(**kwargs)
        elif name == "La Comarca":
            return LaComarca(**kwargs)
        elif name == "Cobreloa":
            return Cobreloa(**kwargs)




    # @property
    # def player(self):
    #     return self.__player

    # @property
    # def opponents(self):
    #     return self.__opponents

    # @property
    # def game_on(self):
    #     return self.__game_on
    
    # @player.setter
    # def player(self, value):
    #     if not isinstance(value, Civilization): raise Exception("Player must be instance of Civilization")
    #     self.__player = value
    
    # @opponents.setter
    # def opponents(self, value):
    #     self.__opponents = value
    
    # def add_player(self, civ):
    #     self.player = civ
    
    # def add_opponent(self, civ):
    #     self.__opponents.append(civ)

    # def play(self):
    #     self.menu.display_options()

    # def create_civilization(self, name, **kwargs):
    #     if name == "DCC":
    #         return DCC(**kwargs)
    #     elif name == "La Comarca":
    #         return LaComarca(**kwargs)
    #     elif name == "Cobreloa":
    #         return Cobreloa(**kwargs)


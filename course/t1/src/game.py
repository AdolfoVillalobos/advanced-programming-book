
from src.civilizacion import Civilization, Cobreloa, DCC, LaComarca
from src.menu import Menu
from src.actions import AttackCivilization, CollectResource, CreatePerson, CreateBuilding


class Game:

    def __init__(self):
        print("Welcome to DCCivilization!\n")
        self.game_on = True
        self.stage = "0_begin"
        self.menu = Menu()

        self.opponents = []
        self.action_queue = []

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
        self.game_setup()
        while self.game_on:
            self.turn()

    def update_menu_key(self, key, valid_range, message=""):
        self.menu.default_options[key] = {valid_range: "Available range"}
        self.menu.default_messages[key] = message

    def show_menu(self):
        self.menu.show_options()

    def update_menu(self, stage_name):
        self.stage = stage_name
        self.menu.stage = stage_name

    def get_input(self):
        self.menu.get_user_input()
        current_input = self.menu.user_input
        return current_input

    def turn(self):
        self.player_turn()
        self.opponent_turn()
    
    def game_setup(self):
        while True:
            self.show_menu()
            current_input = self.get_input()

            if self.stage == "0_begin":
                if current_input == 1:
                    self.update_menu("1_civilization_setup")

                elif current_input == 2:
                    self.update_menu(-1)

            elif self.stage == "1_civilization_setup":
                self.initialize_player(current_input)
                self.initialize_opponents(current_input)
                self.update_menu("2_turn")
                break
    
    def player_turn(self):

        self.apply_actions()
        available_workers = range(0, self.player.num_workers+1)

        while True:
            print(self.stage)
            if self.stage == "2_turn":
                self.show_menu()
                user_input = self.get_input()
                if user_input == 1:
                    self.update_menu("2_turn_a")
                elif user_input == 2:
                    self.update_menu("2_turn_b")
                elif user_input == 3:
                    self.update_menu("2_turn_c")
                elif user_input == 4:
                    self.update_menu("3_turn")
                    break
            elif self.stage == "2_turn_a":
                self.show_menu()
                user_input = self.get_input()

                resource = self.menu.menu_options[user_input]
                self.update_menu_key(key="2_turn_a_numerical",
                                    valid_range=available_workers,
                                    message="Allocate the number of workers:\n")
                self.menu.stage = "2_turn_a_numerical"
                self.show_menu()
                workers = self.get_input()
                action = CollectResource(resource_type=resource,
                                                num_workers=workers,
                                                player_id=self.player.id,
                                                turns_to_completion=1)
                self.action_queue.append(action)
                self.update_menu("2_turn")
            
            elif self.stage == "2_turn_b":
                self.show_menu()
                user_input = self.get_input()
                
                person = self.menu.menu_options[user_input]
                self.menu.stage = "2_turn_b_numerical"
                self.show_menu()
                numerical_input = self.get_input()


            else:
                print("hey")

    def opponents_turn(self):
        pass

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

    def apply_actions(self):
        pass




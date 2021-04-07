from abc import ABC, abstractmethod

# # 0 - New or Load
# # 1 .-  If New -> Select Civilziation. Else, load game.
# # Repeat until game over or exit
# # 2 .- Player Turn
# # 3 .- Opponent Turn

# # Instructions:

# # Player Turn Begining
# # - Show technology advances
# # - Show if been attacked

# # Player Turn Options
# #   - Collect Resources. Available Next Turn
# #   - Create Persons. Available Next Turn
# #   - Create Building. Available in next k-Turns.
# #   - Attack other civilizations. Only one attack.
# #   - End turn
# #   - Go back.

# # Opponent Turn
# # - Actions from actions.csv are executed.

MENU_OPTIONS_BY_STAGE = {
    "0_begin": {1: "New Game", 2: "Load Game"},
    "1_civilization_setup" : {1: "DCC", 2: "La Comarca", 3: "Cobreloa"},
    "2_turn" : {1: "Collect resources", 2: "Create person", 3: "Create building", 4: "End Turn"},
    "2_turn_a" : {1: "Wood", 2: "Stone", 3: "Gold"}, # Collect Resource
    "2_turn_a_numerical" : {"": ""},
    "2_turn_b" : {1: "Worker", 2: "Assistant", 3: "Soldier"}, # Create Person
    "2_turn_c" : {1: "Wall", 2: "Assistant", 3: "Soldier"}, # Create Building
    "numerical_input" : {"x": "Type it!"}
    }

DISPLAY_OPTIONS_BY_STAGE = {
    "0_begin": "Select an Option: \n\n",
    "1_civilization_setup": "Select a Civilization:\n",
    "2_turn": "Your turn. Choose an action: \n",
    "2_turn_a" : "Select a resource to collect: \n",
    "2_turn_a_numerical" : "Type-in: \n",
    "2_turn_b" : "Select a person to create: \n",
    "2_turn_c" : "Select a building o build: \n",
    3: "Now your opponents are playing... \n"
}

class Menu(ABC):

    def __init__(self, default_options=MENU_OPTIONS_BY_STAGE, 
                        default_messages=DISPLAY_OPTIONS_BY_STAGE,
                        ):

        self.default_options = default_options
        self.default_messages = default_messages

    @property
    def menu_options(self):
        return self.default_options[self.stage]
    
    @property
    def display_message(self):
        return self.default_messages[self.stage]
    
    @property
    def user_selection(self):
        return self.__user_selection
    
    @user_selection.setter
    def user_selection(self, value):
        if not value.isnumeric(): raise Exception("User Input Invalid -> Must be an int.")
        value = int(value)
        if not (value in self.menu_options): raise Exception("User Input Invalid -> Try Again.")
        self.__user_selection = value

    def __repr__(self):
        out = ""
        out += self.display_message
        for k, v in self.menu_options.items():
            if isinstance(k, range):
                out += f"\t {v}: [{max(k)}] \n"
            else:
                out += f"\t [{k}] {v}\n"
        return out

    def get_user_input(self):
        valid_input = False
        while not valid_input:
            try:
                self.user_input = input("-> ")
                valid_input = True
            except Exception as e:
                print(e)

class NewGameMenu(Menu):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CollectResourceMenu(Menu):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)



    


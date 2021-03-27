# from src.game import Game

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
    0: {1: "New Game", 2: "Load Game"},
    1 : {1: "DCC", 2: "La Comarca", 3: "Cobreloa"},
    2 : {1: "Collect resources", 2: "Create person", 3: "Create building", 4: "End Turn"}
    }

DISPLAY_OPTIONS_BY_STAGE = {
    0 : "Select an Option: \n\n",
    1: "Select a Civilization:\n",
    2: "Your turn. Choose an action: \n",
    3: "Now your opponents are playing... \n"
}

class Menu:

    def __init__(self, initial_stage = 0):
        self.stage = initial_stage

    @property
    def stage(self):
        return self.__stage

    @property
    def menu_options(self):
        return MENU_OPTIONS_BY_STAGE[self.stage]
    
    @property
    def display_message(self):
        return DISPLAY_OPTIONS_BY_STAGE[self.stage]
    
    @property
    def user_input(self):
        return self.__user_input

    # Setters
    @stage.setter
    def stage(self, value):
        self.__stage = value

    @user_input.setter
    def user_input(self, value):
        if not value.isnumeric(): raise Exception("User Input Invalid -> Must be an int.")
        value = int(value)
        if not value in self.menu_options: raise Exception("User Input Invalid -> Try Again.")
        self.__user_input = value

    def show_options(self):
        out = ""
        out += self.display_message
        for k, v in self.menu_options.items():
            out += f"\t [{k}] {v}\n"
        print(out)

    def get_user_input(self):
        valid_input = False
        while not valid_input:
            try:
                self.user_input = input("-> ")
                valid_input = True
            except Exception as e:
                print(e)



# class Menu:
#     def __init__(self):
#         self.game = Game()
#         self.__user_input = None
#         self.__options = None

#         print("Welcome to the DCCivilization Game!")

#         # Initiate the game

#         self.stage = 0
#         self.display_message = "Select an Option:\n"
#         self.menu_options = {1: "New Game", 2: "Load Game"}



#     @property
#     def user_input(self):
#         return self.__user_input

#     @property
#     def stage(self):
#         return self.__stage
    
#     @property
#     def menu_options(self):
#         return self.__menu_options

#     @user_input.setter
#     def user_input(self, value):
#         if not value.isnumeric(): raise Exception("User Input Invalid -> Must be an int.")
#         value = int(value)
#         if not value in self.menu_options: raise Exception("User Input Invalid -> Try Again.")
#         self.__user_input = value

#     @menu_options.setter
#     def menu_options(self, value):
#         if not isinstance(value, dict): raise Exception("Options must be Dict.")
#         self.__menu_options = value

#     @stage.setter
#     def stage(self, value):
#         self.__stage = value

#     def update_menu(self):
#         if self.stage == 0:
#             self.display_message = "Select an Option:\n"
#             self.menu_options = {1: "New Game", 2: "Load Game"}
#         elif self.stage == 1:
#             self.display_message = "Select a Civilization: \n"
#             self.menu_options = {1: "DCC", 2: "La Comarca", 3: "Cobreloa"}

#         elif self.stage == 2:
#             self.display_message = "Your Turn!: \n"
#             self.menu_options = {1: "Collect resources", 
#                                 2: "Create person",
#                                 3: "Create building",
#                                 4: "End Turn"}

#     def get_user_input(self):
#         valid_input = False
#         while not valid_input:
#             try:
#                 self.user_input = input("-> ")
#                 valid_input = True
#             except Exception as e:
#                 print(e)

#     def execute_user_input(self):
#         print(f"You have selected option:  {self.menu_options[self.user_input]}\n")
#         if self.stage == 0:
#             if self.user_input == 1:
#                 self.stage = 1
#         elif self.stage == 1:
#             for _id, civ_name in self.menu_options.items():
#                 civ = self.game.create_civilization(civ_name, id=_id)
#                 if _id == self.user_input:
#                     self.game.add_player(civ)
#                 else:
#                     self.game.add_opponent(civ)
#             self.stage = 2
#         elif self.stage == 2:
            

#         self.update_menu()


#     def show_game(self):
#         print(self.game.player)

#     def __repr__(self):
#         out = ""
#         out += self.display_message
#         for k, v in self.menu_options.items():
#             out += f"\t [{k}] {v}\n"
#         return out




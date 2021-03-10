class Resources:
    def __init__(self):
        self._gold = 0
        self._wood = 0
        self._stone = 0
    
    @property
    def gold(self):
        return self._gold

    @property
    def wood(self):
        return self._wood

    @property
    def stone(self):
        return self._stone

    @gold.setter
    def gold(self, value):
        self._gold = value
 
    @wood.setter
    def wood(self, value):
        self._wood = value
 
    @stone.setter
    def stone(self, value):
        self._stone = value
 
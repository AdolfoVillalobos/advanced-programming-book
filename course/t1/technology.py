from abc import ABC, abstractmethod

class Technology(ABC):
    def __init__(self, required_points):
        self.has_been_implemented = False

    @property
    @abstractmethod
    def required_points(self):
        pass
    
class Mathematics(Technology):
    @property
    def required_points(self):
        return 30
    
class Education(Technology):
    @property
    def required_points(self):
        return 30

class Medicine(Technology):
    @property
    def required_points(self):
        return 140

class Computation(Technology):
    @property
    def required_points(self):
        return 250



    
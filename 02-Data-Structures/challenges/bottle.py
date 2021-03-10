class Bottle:
    def __init__(self, liters=1):
        self.liters = liters

    @property
    def label(self):
        return "DCC-cola"
    
    def __str__(self):
        return f"{self.liters} liters of {self.label}."

## Aux functions

def __mean(data):
    return sum(data)/len(data)

def _var(data):
    mu = _mean(data)
    ss = sum([ (x-mu)**2 for x in data])
    return ss/(len(data)-1)


class Observation:

    def __init__(self,  magnitude, time, error):
        self.time = time
        self.magnitude = magnitude
        self.error = error

class Star:

    def __init__(self,  variability_class, _id, RA, DEC, observations=None):
        self._id = _id
        self.variability_class = variability_class 
        self.RA = RA
        self.DEC = DEC

        if observations is None:
            observations = []
        self.observations = observations
        
    def get_magnitudes(self):
        return [o.magnitude for o in self.observations]

    def average_brightness(self):
        magnitudes = self.get_magnitudes()
        return _mean(magnitudes)

    def var_brightness(self):
        magnitudes = self.get_magnitudes()
        return _var(magnitudes)

    def add_observation(self, time, magnitude, error):
        self.observations.append(Observation(time, magnitude, error))

class Field:

    def __init__(self, stars=None):
        if stars is None:
            stars = []
        self.stars = []

    def add_star(self, star):
        self.stars.append(star) # Stars are independant of fields

class Sky:

    def __init__(self, fields=None):
        if fields is None:
            fields = []
        self.fields = fields

    def add_field(self, field):
        self.fields.append(field)


if __name__ == "__main__":

    sky = Sky()

    e0 = Star( "RRLyrae", 0, 0,0, [Observation(2, 1000, (1,3)),
                                Observation(3, 1000, (3,3)),
                                Observation(4, 1000, (4,3))])
    e1 = Star( "Cepheids", 1, 4,5 , [Observation(5, 1000, (1,3)),
                                Observation(6, 1000, (3,3)),
                                Observation(7, 1000, (4,3))])
    e2 = Star( "Mira", 2, 10,1000, [Observation(10, 1000, (1,3)),
                                Observation(11, 1000, (3,3)),
                                Observation(12, 1000, (4,3))])

    e3 = Star('Cepheids', 50, 15, 3)
    e4 = Star('Cepheids', 120, 120, 4)
    e5 = Star('Eclipsing Binaries', 0, 90, 5)


    
    f0 = Field()

    e3.add_observation(21, 1000, (15, 30))
    e3.add_observation(22, 1000, (15, 30))
    e3.add_observation(23, 1000, (15, 30))
    e4.add_observation(24, 1000, (15, 30))
    e4.add_observation(25, 1000, (15, 30))
    e4.add_observation(26, 1000, (15, 30))
    e5.add_observation(27, 1000, (15, 30))
    e5.add_observation(28, 1000, (15, 30))
    e5.add_observation(29, 1000, (15, 30))


    f0.add_star(e1)
    f0.add_star(e2)
    f0.add_star(e3)

    sky.add_field(f0)
    sky.add_field(Field([e0, e4, e5]))



    print(sky.fields[0].stars[0].get_magnitudes())

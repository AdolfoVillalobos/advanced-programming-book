from collections import deque
from random import choice, randrange

class Vehicle:
    tp = {"motorcycle": 10, "car": 25, "suv": 30}

    def __init__(self):
        self.vehicle_type = choice(list(Vehicle.tp))
        self._testing_time = Vehicle.tp[self.vehicle_type]

    @property
    def testing_time(self):
        return self._testing_time

    @testing_time.setter
    def testing_time(self, new_time):
        self._testing_time = new_time
    
    def show_type(self):
        print(f"Testing: {self.vehicle_type}.")

class Plant:

    def __init__(self, vehicles_per_hour):
        self.test_ratio = vehicles_per_hour
        self.current_task = None
        self.testing_time = 0


    def busy(self):
        return self.current_task != None

    def next_vehicle(self, vehicle):

        self.current_task = vehicle
        self.testing_time = self.current_task.testing_time
        self.current_task.show_type()

    def tick(self):
        if self.current_task != None:
            self.testing_time = self.testing_time -1
            if self.testing_time <= 0:
                self.current_task = None

def arrive_new_car():

    num = randrange(1, 201)
    return num == 200

def testing():

    plant = Plant(5)

    # Empty queue
    q = deque()

    # Waiting time
    time_list = []

    # We model the arrival of cars:
    for instant in range(1000):
        if arrive_new_car():
            v = Vehicle()
            q.append(v)

        if (not plant.busy()) and (len(q) >0):
            # We get the next vehicle in the queue

            next_vehicle = q.popleft()
            time_list.append(next_vehicle.testing_time)
            plant.next_vehicle(next_vehicle)

    # We make time pass by one tick
        plant.tick()

    average_time = sum(time_list)/len(time_list)
    print(f"Average waiting time: {average_time} min, {len(time_list)} vehicles queued.")

if __name__ == "__main__":
    testing()

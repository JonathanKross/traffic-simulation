import math
import random
import statistics as st
import matplotlib.pyplot as plt
import numpy as np


class Simulation:

    def __init__(self):
        self.ticks = 0
        self.road = Road()


class Car:

    def __init__(self, max_speed=33, location=0, speed=0):
        self.max_speed = max_speed
        self.location = location
        self.speed = speed
        self.tailing_distance = 0
        self.next_car = 0


    def __str__(self):
        return "Location= {}, Speed= {}, Dist= {}".format(self.location, self.speed, self.tailing_distance)


    def __repr__(self):
            return self.__str__()


    def accelerate(self):
        self.speed += 2


    def decelerate(self):
        self.speed -= 2


    def random_slowdown(self):
        random_number = random.randint(1, 10)
        if random_number == 1 and self.speed <= 1:
                self.speed = 0
                return True
        elif random_number == 1:
                self.decelerate()
                return True
        else:
            return False

        # if random.random() < .10:
        #     if self.speed > 2:
        #         self.speed -= 2


    def calculate_new_speed(self, slow):
        if slow == False:

            if self.tailing_distance <= 2:
                self.speed = 0

            elif self.tailing_distance >= self.speed and self.speed < self.max_speed:
                self.accelerate()

            else:
                self.speed = self.next_car.speed


    def change_car_location(self):
        self.location += self.speed
        if self.location > 1000:
            self.location = self.location % 1000
        return self.location


    def set_tailing_distance_attr(self):

        if self.next_car.location - self.location < 0:
            self.tailing_distance = self.next_car.location - ((self.location + 5) - 1000)
        else:
            self.tailing_distance = self.next_car.location - (self.location + 5)


    def update_speed(self, space, next_car):
        """Change the car's speed based on space ahead of car."""
        if space <= 2:
            self.speed = 0
        elif space >= self.speed and self.speed < self.max_speed:
            # if self.speed < self.max_speed:
            self.speed += self.acceleration
            # elif self.speed > self.max_speed:
            #     self.speed = self.max_speed
        else:
            self.speed = next_car.speed

    # def list_locations(self):
    #     return sorted([car.location for car in road.cars])
    #
    #
    # def determine_distance(self):
    #
    #     list_locations = road.list_locations()
    #
    #     car_index = list_locations.index(self.location)
    #
    #     next_car_index = car_index + 1
    #
    #     try:
    #         next_car_location = list_locations[next_car_index]
    #         self.tailing_distance = (next_car_location - (car.location + 5))
    #
    #     except IndexError:
    #         next_car_location = list_locations[0]
    #         self.tailing_distance = (next_car_location) - ((car.location + 5) - 1000)

class Road:

    def __init__(self):
        self.cars = [Car() for _ in range(30)]
        self.graph = np.array([0 for _ in range(1100)])


    def inital_car_location(self):
        """1000/30 = 33.33. Evenly space cars. ~28 meters between cars initally"""

        initiation = 1
        for car in self.cars:
            car.location = initiation
            initiation += 33


    def set_next_car_attr(self):

        for i, car_obj in enumerate(self.cars):
            if i == 29:
                car_obj.next_car = self.cars[0]
            else:
                car_obj.next_car = self.cars[i + 1]


    # def random_slowdown(self):
    #     random_number = random.randint(1, 10)
    #     if random_number == 1 and self.speed <= 1:
    #             self.speed = 0
    #             return True
    #     elif random_number == 1:
    #             self.decelerate()
    #             return True
    #
    #
    # def calculate_new_speed(self, slow):
    #     if not slow:
    #
    #         if self.tailing_distance <= 2:
    #             self.speed = 0
    #
    #         elif self.tailing_distance > self.speed and self.speed < self.max_speed:
    #             self.accelerate()
    #
    #         else:
    #             self.decelerate()
    #
    #
    # def list_locations(self):
    #     return sorted([car.location for car in self.cars])
    #
    #
    # def determine_distance(self, car):
    #
    #     list_positions = self.list_locations()
    #
    #     car_index = list_positions.index(car.location)
    #
    #     next_car_index = car_index + 1
    #
    #     try:
    #         next_car_location = list_positions[next_car_index]
    #         car.tailing_distance = (next_car_location - (car.location + 5))
    #
    #     except IndexError:
    #         next_car_location = list_positions[0]
    #         car.tailing_distance = (next_car_location) - ((car.location + 5) - 1000)
    # def move_all_car_locations(self):
    #     return [car.change_car_location() for car in self.cars]
    #
    #
    # def list_speeds(self):
    #     return [car.speed for car in self.cars]


def main():
    sim = Simulation()
    sim.road.inital_car_location()
    sim.road.set_next_car_attr()

    list_all_locations = []
    list_avg_speeds = []

    ticks = 1

    while ticks <= 60:
        for car_obj in sim.road.cars:

            print('Tick:', ticks)

            car_obj.set_tailing_distance_attr()
            slow = car_obj.random_slowdown()
            car_obj.calculate_new_speed(slow)
            car_obj.change_car_location()

            print('Location', car_obj.location, 'Tailing', car_obj.tailing_distance, 'Speed', car_obj.speed)

        list_all_locations.append([car_obj.location for car_obj in sim.road.cars])
        list_avg_speeds.append(round(sum([car_obj.speed for car_obj in sim.road.cars])/30.0, 2))
        ticks += 1

    print("\n\n\n\n", list_all_locations)
    print("\n\n\n\n", list_avg_speeds)


    x = list_all_locations
    y = [n for n in range(60)]
    plt.scatter(x,y)
    plt.show()

if __name__ == "__main__":
    main()



# for car_obj in sim.road.cars:
#     print('Next Car:',car_obj.next_car)
#
# for car_obj in sim.road.cars:
#     car_obj.set_tailing_distance_attr()
#     print('Tailing Distance:',car_obj.tailing_distance)

# ticks = 1
# list_all_locations = []
# list_all_speeds = []
#
# while ticks <= 2:
#     print(sim.road.cars)
#     print("-------------------")
#     for car_obj in sim.road.cars:
#         # list_of_locations = sim.road.list_locations()
#         sim.road.determine_distance(car_obj)
#
#     for car_obj in sim.road.cars:
#         slow = car_obj.random_slowdown()
#         car_obj.calculate_new_speed(slow)
#     print(sim.road.cars)
#     print("-------------------")
#
#
#     for car_obj in sim.road.cars:
#         car_obj.change_car_location()
#         # car.time += 1
#     print(sim.road.cars)
#     print("-------------------")
#
#     list_all_locations.append([car_obj.location for car_obj in sim.road.cars])
#     list_all_speeds.append(sum([car_obj.speed for car_obj in sim.road.cars])/30.0)
#
#     ticks += 1
#
# print("\n\n\n\n", list_all_speeds)
# print("\n\n\n\n", list_all_locations)
# sim = Simulation()
# sim.road.inital_car_location()
# print(sim.road.cars)
#
# listy = sim.road.list_locations()
# for car in sim.road.cars:
#     sim.road.determine_distance(car)
# print(sim.road.cars)

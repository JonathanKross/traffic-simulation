import math
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn
import statistics as st


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
        return "Location= {}, Speed= {}, Dist= {}".format(
            self.location, self.speed, self.tailing_distance)

    def __repr__(self):
            return self.__str__()

    def accelerate(self):
        """Increase a car's speed by 2 m/s."""
        self.speed += 2

    def decelerate(self):
        """Decrease a car's speed by 2 m/s."""
        self.speed -= 2

    def random_slowdown(self):
        """10 percent random slow requirement of 2m/s."""
        random_number = random.randint(1, 10)
        if random_number == 1 and self.speed <= 1:
                self.speed = 0
                return True
        elif random_number == 1:
                self.decelerate()
                return True
        else:
            return False

    def calculate_new_speed(self, slow):
        """Based on distance between cars, calculates car's new speed."""
        if slow is False:

            if self.tailing_distance <= 2:
                self.speed = 0

            elif self.tailing_distance >= self.speed and self.speed < self.max_speed:
                self.accelerate()

            else:
                self.speed = self.next_car.speed

    def change_car_location(self):
        """Move a car's position based on speed. Check for going past 1km."""
        self.location += self.speed
        if self.location > 1000:
            self.location = self.location % 1000
        return self.location

    def set_tailing_distance_attr(self):
        """Find distance in meters between each car and set as self attr."""
        if self.next_car.location - self.location < 0:
            self.tailing_distance = self.next_car.location - (
                                                    (self.location + 5) - 1000)
        else:
            self.tailing_distance = self.next_car.location - (self.location + 5)

    def update_speed(self, space, next_car):
        """Change the car's speed based on space ahead of car."""
        if space <= 2:
            self.speed = 0
        elif space >= self.speed and self.speed < self.max_speed:
            self.speed += self.acceleration
        else:
            self.speed = next_car.speed


class Road:

    def __init__(self):
        self.cars = [Car() for _ in range(30)]

    def inital_car_location(self):
        """1000/30 = 33 Evenly space cars. ~28 meters between cars initally."""
        initiation = 1
        for car in self.cars:
            car.location = initiation
            initiation += 33

    def set_next_car_attr(self):
        """Set the self attr of next_car as the Car object in front of self."""
        for i, car_obj in enumerate(self.cars):
            if i == 29:
                car_obj.next_car = self.cars[0]
            else:
                car_obj.next_car = self.cars[i + 1]


def main():
    sim = Simulation()
    sim.road.inital_car_location()
    sim.road.set_next_car_attr()

    list_avg_speeds = []

    ticks = 1

    while ticks <= 60:
        for car_obj in sim.road.cars:

            car_obj.set_tailing_distance_attr()
            slow = car_obj.random_slowdown()
            car_obj.calculate_new_speed(slow)
            car_obj.change_car_location()

        x = [car_obj.location for car_obj in sim.road.cars]
        y = [n for n in range(len(x))]
        plt.scatter(x, y)

        list_avg_speeds.append(round(st.mean(
                        [car_obj.speed for car_obj in sim.road.cars]), 2))
        ticks += 1

    plt.show()

if __name__ == "__main__":
    main()

import math
import random
import statistics as st
import matplotlib.pyplot as plt
import numpy as np


class Simulation:

    def __init__(self):
        self.ticks = 0
        self.road = Road()

    def tick(self):
        # all cars change speed
        # all cars change position
        pass

    def sim(self, time = 60):
        pass


class Car:

    def __init__(self, max_speed=33, speed=0, position=0):
        self.max_speed = max_speed
        self.speed = speed
        self.position = position

    def __str__(self):
        return "Position= {}".format(self.position)

    def __repr__(self):
            return self.__str__()

    def change_position(self):
        self.position += self.speed
        if self.position > 1000:
            self.position = self.position % 1000
        return self.position



class Road:

    def __init__(self):
        self.cars = [Car() for _ in range(30)]
        self.graph = np.array([0 for _ in range(1100)])



    def inital_car_position(self):
        """1000/30 = 33.33. Evenly space cars. ~28 meters between cars initally"""
        initiation = 0
        for car in self.cars:
            car.position = initiation
            initiation += 33


    def change_speeds(self):
        #if random.random? car.speed -= 2
        #if distance large enough? car.speed += 2
        #if distance large enough, but car.speed == max_speed
        #if distance not large enough... car.speed  -= 2?
        #if distance
        pass


    def move_all_car_positions(self):
        pass


    def list_positions(self):
        pass


    def list_speeds(self):
        pass


sim = Simulation()
sim.road.inital_car_position()
print(sim.road.cars)

#!/usr/bin/env python3

import random
import time

GROWTH_CONST = 2
PLANT_LIST = ["Rose", "Sun Flower", "Violet", "Banana Tree", "Dendelion"]

class Plant:

    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age
        msg = f"Planting a {self._name:12} of height {self._height}cm and {self._age} days old."
        print(msg)

    def age(self):
        self._age += 1

    def grow(self):
        self._height += GROWTH_CONST
    
    def day_update(self):
        self.age()
        self.grow()

    def get_info(self):
        return self._name, self._height, self._age 

    def display_info(self):
        print(f"Plant: {self._name:12} | Height: {self._height:8}cm | Age: {self._age:8} days")

def display_plant_infos(plant:Plant):
    name, height, age = plant.get_info()
    print(f"Plant: {name:10} | Height: {height}cm | Age: {age} days")

def simulate_day_in_garden(garden:list):
    for p in garden:
        p.day_update()

def display_garden_info(garden:list):
    for p in garden:
        p.display_info()

def plant_random_garden(size:int):
    garden = []
    random.seed(int(time.time()))
    
    for i in range(size):
        c_plant = PLANT_LIST[i % (len(PLANT_LIST))]
        c_h, c_a = int(random.random() * 300), int(random.random() * 30)
        garden.append(Plant(c_plant, c_h, c_a))
    
    print(f"Total plants planted: {size}\n")
    
    return garden

def main():
    garden = plant_random_garden(10)

    print("=== Garden Plant Registry ===")
    display_garden_info(garden)

    # print("\n=== Growth Simulation ===\n")
    # print("=== Day 1 ===")
    # display_garden_info(garden)
    # for i in range(7):
    #     simulate_day_in_garden(garden)
    # print("=== Day 7 ===")
    # display_garden_info(garden)





if __name__ == "__main__":
    main()
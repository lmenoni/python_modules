#!/usr/bin/env python3

import random
import time

GROWTH_CONST = 2
PLANT_LIST = ["Rose", "Sun Flower", "Violet", "Banana Tree", "Dendelion"]

class SecurePlant:

    def __init__(self, name, height, age):
        self._name = name
        self.s_height = height
        self.s_age = age
        print(f"Plant created: {self._name}")

    # --- Property for height ---
    @property
    def s_height(self):
        return self._height
    
    @s_height.setter
    def s_height(self, value):
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            if hasattr(self, '_height'):
                 print(f"Height updated: {value}cm [OK]")

    @property
    def s_age(self):
        return self._age

    @s_age.setter
    def s_age(self, value):
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            if hasattr(self, '_age'):
                print(f"Age updated: {value} days [OK]")

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
        print(f"Plant: {self._name:12} | Height: {self.s_height:8}cm | Age: {self.s_age:8=} days")


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
        garden.append(SecurePlant(c_plant, c_h, c_a))
    
    print(f"Total plants planted: {size}\n")
    
    return garden

def main():
    garden = plant_random_garden(10)

    print("=== Garden Plant Registry ===")
    display_garden_info(garden)

    print("\n=== Bad sets ===\n")
    garden[0].s_height = 10
    garden[0].s_age = 10
    garden[0].display_info()
    garden[0].s_age = -5


    # print("\n=== Growth Simulation ===\n")
    # print("=== Day 1 ===")
    # display_garden_info(garden)
    # for i in range(7):
    #     simulate_day_in_garden(garden)
    # print("=== Day 7 ===")
    # display_garden_info(garden)





if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import random
import time

GROWTH_CONST = 2
PLANT_LIST = ["Rose", "Sun Flower", "Violet", "Banana Tree", "Dendelion"]

class Plant:

    def __init__(self, name, height, age):
        self._name = name
        self.height = height
        self.age = age

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
        else:
            self._height = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
        else:
            self._age = value

    def get_info(self):
        return self._name, self.height, self.age 

    def display_info(self):
        print(f"Plant: {self._name:12} | Height: {self._height:8}cm | Age: {self._age:8} days")


class Flower(Plant):

    def __init__(self, name, height, age, flower_color):
        super().__init__(name, height, age)
        self._flower_color = flower_color
    
    def bloom(self):
        print(f"{self._name.capitalize()} is blooming beautifully!\n")
    
    def display_info(self):
        print(f"\n{self._name.capitalize()} (Flower): {self.height}cm, {self.age} days, {self._flower_color} color")
        self.bloom()
    
class Tree(Plant):

    def __init__(self, name:str, height:int, age:int, trunk_diameter:int):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
    
    def produce_shade(self):
        area = (self.height / 100) * (self._trunk_diameter / 100)
        print(f"{self._name.capitalize()} provides {area} square meters of shade\n")
    
    def display_info(self):
        print(f"\n{self._name.capitalize()} (Tree): {self.height}cm, {self.age} days, {self._trunk_diameter}cm diameter")
        self.produce_shade()

class Vegetable(Plant):

    def __init__(self, name, height, age, harvest_season:str, nutritional_value:str):
        super().__init__(name, height, age)
        self._nutritional_value = nutritional_value
        self._harvest_season = harvest_season
    
    def tell_nutrition(self):
        print(f"{self._name.capitalize()} is rich in {self._nutritional_value}\n")
    
    def display_info(self):
        print(f"\n{self._name.capitalize()} (Vegetable): {self.height}cm, {self.age} days, {self._harvest_season} harvest")
        self.tell_nutrition()

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
    garden = []

    garden.append(Flower("rose", 25, 30, "red"))
    garden.append(Tree("oak", 500, 1825, 50))
    garden.append(Vegetable("tomato", 80, 90, "summer", "vitamin C"))


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
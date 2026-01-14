#!/usr/bin/env python3

GROWTH_CONST = 2

class Plant:

    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age

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
        print(f"Plant: {self._name:10} | Height: {self._height}cm | Age: {self._age} days")

def display_plant_infos(plant:Plant):
    name, height, age = plant.get_info()
    print(f"Plant: {name:10} | Height: {height}cm | Age: {age} days")

def simulate_day_in_garden(garden:list):
    for p in garden:
        p.day_update()

def display_garden_info(garden:list):
    for p in garden:
        p.display_info()

def main():
    garden = []

    print("=== Garden Plant Registry ===")
    garden.append(Plant("Rose", 25, 20))
    garden.append(Plant("Sunflower", 33, 24))
    garden.append(Plant("Bush", 15, 35))

    display_garden_info(garden)

    print("\n=== Growth Simulation ===\n")
    print("=== Day 1 ===")
    display_garden_info(garden)
    for i in range(7):
        simulate_day_in_garden(garden)
    print("=== Day 7 ===")
    display_garden_info(garden)





if __name__ == "__main__":
    main()
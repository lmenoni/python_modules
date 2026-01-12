#!/usr/bin/env python3

class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        print(f"Plant: {self.name:10} | Height: {self.height}cm | Age: {self.age} days")

def main():
    garden = []

    print("=== Garden Plant Registry ===")
    garden.append(Plant("Rose", 25, 20))
    garden.append(Plant("Sunflower", 33, 24))
    garden.append(Plant("Bush", 15, 35))

    for p in garden:
        p.display_info()




if __name__ == "__main__":
    main()


class Plant:

    def __init__(self, name:str, height:int):
        self._name = name
        self._height = height
    
    def info(self):
        return f"{self._name.capitalize()}: {self._height}cm"
    
    def grow(self, value:int):
        self._height += 1
        print(f"{self._name.capitalize()} grew {value}cm")
    
class FloweringPlant(Plant):

    def __init__(self, name:str, height:int, color:str):
        super().__init__(name, height)
        self._color = color

    def info(self):
        return f"{self._name.capitalize()}: {self._height}cm, {self._color} flowers (blooming)"

class PrizeFlower(FloweringPlant):

    def __init__(self, name:str, height:int, color:str, prize:int):
        super().__init__(name, height, color)
        self._prize = prize

    def info(self):
        return f"{self._name.capitalize()}: {self._height}cm, {self._color} flowers (blooming), Prize points: {self._prize}"


class Garden:

    def __init__(self, owner:str, plants:list = None):
        self._owner = owner
        self._plants = []
        self._size = 0
        self._plants_added = 0
        self._total_growth = 0
        if plants:
            for p in plants:
                self._plants.append(p)
                self._size += 1

    def add_plant(self, plant:Plant):
        self._plants.append(plant)
        self._size += 1
        self._plants_added += 1

    def grow_garden(self, value:int):
        for p in self._plants:
            p.grow(value)
            self._total_growth += 1

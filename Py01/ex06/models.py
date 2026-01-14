

class Plant:

    def __init__(self, name:str, height:int, age:int):
        self._name = name
        self._height = height
        self._age = age
    
    def info(self):
        return f"{self._name.capitalize()}: {self._height}cm"
    
class FloweringPlant(Plant):

    def __init__(self, name:str, height:int, age:int, color:str):
        super().__init__(name, height, age)
        self._color = color

    def info(self):
        return f"{self._name.capitalize()}: {self._height}cm, {self._color} flowers (blooming)"

class PrizeFlower(FloweringPlant):
    """
    Docstring for PrizeFlower
    """
    def __init__(self, name:str, height:int, age:int, color:str, prize:int):
        super().__init__(name, height, age, color)
        self._prize = prize

    def info(self):
        return f"{self._name.capitalize()}: {self._height}cm, {self._color} flowers (blooming), Prize points: {self._prize}"
    
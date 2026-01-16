from models import Garden
from models import PrizeFlower
from models import FloweringPlant
from models import Plant

import random

TYPES_DICT = [Plant, FloweringPlant, PrizeFlower]

class GardenManager:

    def __init__(self):
        self._gardens = {}
    
    class GardenStats:

        @staticmethod
        def report_garden(garden:Garden):
            if not garden:
                print("Trying to report an inexistent garden")
                return
            
            print(f"=== {garden._owner.capitalize()}'s Garden Report ===")
            plants = garden._plants
            reg_c = 0
            flo_c = 0
            pri_c = 0

            print("Plants in garden:")
            for p in plants:
                print(f"- {p.info()}")

                if type(p) is PrizeFlower:
                    pri_c += 1
                elif type(p) is FloweringPlant:
                    flo_c += 1
                elif type(p) is Plant:
                    reg_c += 1
            
            print("\n")
            print(f"Plants added: {garden._plants_added}, Total growth: {garden._total_growth}cm")
            print(f"Plant types: {reg_c} regular, {flo_c} flowering, {pri_c} prize flowers\n")
        
        @staticmethod
        def calculate_score(g:Garden):
            plants = g._plants
            score = 0

            for p in plants:
                score += p._height
                if type(p) is PrizeFlower:
                    score += p._prize
            
            return score

        @classmethod
        def get_scores(cls, gs:dict):
            res = {}

            for o in gs:
                res[o] = cls.calculate_score(gs[o])
            
            return res



    def print_scores(self):
        scores_dict = self.GardenStats.get_scores(self._gardens)

        msg = "Gardens scores - "
        first = True
        for o_name in scores_dict:
            if first:
                first = not first
            else:
                msg += ", "
            
            msg += f"{o_name.capitalize()}: {scores_dict[o_name]}"
        
        print(msg)
    
    def n_gardens(self):
        return len(self._gardens)

    def new_garden(self, owner:str, garden:Garden = None):
        self._gardens[owner] = garden if garden else Garden(owner)
    
    def add_plant_to_garden(self, owner:str, plant:Plant):
        if owner not in self._gardens:
            self.new_garden(owner)

        self._gardens[owner].add_plant(plant)
        print(f"Added {plant._name.capitalize()} to {owner.capitalize()}'s garden")
    
    def owner_grow_garden(self, owner:str):
        if (owner not in self._gardens):
            print(f"[{owner}] Owner not in gardens list")
            return
        
        print(f"{owner.capitalize()} is helping all plants grow...")
        self._gardens[owner].grow_garden(1)

    def print_owner_report(self, owner:str):
        if (owner not in self._gardens):
            print(f"[{owner}] Owner not in gardens list")
            return
        
        self.GardenStats.report_garden(self._gardens[owner])


    @classmethod
    def create_garden_network(cls, gardens:dict):
        manager = cls()
        for owner in gardens:
            manager.new_garden(owner, gardens[owner])
        
        return manager
    
    @staticmethod
    def validate_height(value:int):
        return value >= 0

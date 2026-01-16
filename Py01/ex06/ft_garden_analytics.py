#!/usr/bin/env python3

import random
import time


from manager import GardenManager
import models



def main():
    own1 = "alice"
    own2 = "bob"
    bob_plants = [models.Plant("oak tree", 92)]
    gdict = {own1:None, own2:models.Garden(own2, bob_plants)}
    manager = GardenManager.create_garden_network(gdict)

    print("=== Garden Management System Demo ===\n")

    manager.add_plant_to_garden(own1, models.Plant("oak tree", 100))
    manager.add_plant_to_garden(own1, models.FloweringPlant("rose", 25, "red"))
    manager.add_plant_to_garden(own1, models.PrizeFlower("sunflower", 50, "yellow", 10))
    print("\n")

    manager.owner_grow_garden(own1)
    print("\n")

    manager.print_owner_report(own1)

    print(f"Height validation test:", GardenManager.validate_height(-5))
    manager.print_scores()
    print(f"Total gardens managed: {manager.n_gardens()}")




if __name__ == "__main__":
    main()

VALID_UNITS = {"grams":"grams total", "packets":"packets available", "area":"square meters"}

def ft_seed_inventory(seed_type:str, quantity:int, unit:str):
    if (unit not in VALID_UNITS):
        print("Unkown type.")
        return
    seed_type = seed_type.capitalize()
    bridge = ": "
    if (unit == "area"):
        bridge += "covers"
    print(seed_type + bridge, quantity, VALID_UNITS[unit])

    return
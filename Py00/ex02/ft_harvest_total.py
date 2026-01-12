
def ft_harvest_total():
    idx = 1
    tot = 0


    c = int(input("Day 1 harvest: "))
    tot += c
    c = int(input("Day 2 harvest: "))
    tot += c
    c = int(input("Day 3 harvest: "))
    tot += c

    print("Total harvest:", tot)
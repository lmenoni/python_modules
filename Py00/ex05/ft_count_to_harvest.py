

def recur_count(day = 1):
    if (day > 5):
        return
    elif (day == 1):
        print("Days until harvest: 5")
    print("Day", day)
    recur_count(day + 1)
    if (day == 5):
        print("Harvest time!")

def iter_count():
    day = 1

    print("Days until harvest: 5")
    while day <= 5:
        print("Day", day)
        day += 1
    print("Harvest time!")
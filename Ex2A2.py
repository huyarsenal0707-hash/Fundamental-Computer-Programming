def cabin_class():
    describe_cabin = str(input("Enter cabin class : "))
    if describe_cabin == "LUX":
        print("upper-deck cabin with a balcony")
    elif describe_cabin == "A":
        print("above the car deck, equipped with a window")
    elif describe_cabin == "B":
        print("windowless cabin above the car deck")
    elif describe_cabin == "C":
        print("windowless cabin below the car deck")
    else:
        print("Invalid cabin class")
cabin_class()
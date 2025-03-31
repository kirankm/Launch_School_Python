def number_range(val):
    if (val >= 0) and (val <= 50):
        print("the value is between 0 and 50")
    elif (val >= 0) and (val <= 100):
        print("the value is between 51 and 100")
    elif val > 100:
        print("the value is greater than 100")
    else:
        print("the value is less than 0")

number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0
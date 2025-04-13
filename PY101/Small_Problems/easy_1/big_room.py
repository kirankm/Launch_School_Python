length = input("give the length of the room in metres: ")
breadth = input("give the breadth of the room in metres: ")

area_in_sqm = float(length) * float(breadth)
area_in_sqf = area_in_sqm * 10.7639

print(f"Area in Square Metres is : {area_in_sqm}")
print(f"Area in Square Feet is : {area_in_sqf}")
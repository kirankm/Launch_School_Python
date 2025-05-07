DEGREE = "\u00B0"

def dms(angle):
    normalized_angle = angle % 360
    degree = int(normalized_angle)
    
    minute_second = 60 * (normalized_angle - degree)
    minute = int(minute_second)

    second = int(60 * (minute_second - minute))

    return f"{degree}{DEGREE}{minute:02d}'{second:02d}\""



# print(dms(30))
# print(dms(93.034773))# == "93°02'05\"")
# print(dms(0))# == "0°00'00\"")
# `print(dms(360))# == "360°00'00\"" or dms(360) == "0°00'00\"")

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
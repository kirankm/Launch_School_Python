# for i in range(0,99):
#     if i % 2 == 0:
#         print(i + 1)

start_int = int(input("Give start of the range: "))
end_int = int(input("Give end of the range: "))
for i in range(start_int,end_int, 2):
    if i%2 == 0:
        print(i + 1)


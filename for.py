

# for x in range(1,11, 4):
#     #range() function takes three args start. end (non-inclusive),and a step
#     print(x)

# for x in range(10, 0, -1):
#     print(x)

# there is another, more elegant, way to count down
# for x in reversed((range(1,11))):
#     print(x)

# for x in range(1,15):
#     if x == 13:
#         break
#     else:
#         print(x)

for x in range(1,15):
    if x % 2 == 0:
        continue
    else:
        print(x)

for x in range(1,16):
    if x % 2 > 0:
        continue
    else:
        print(x)
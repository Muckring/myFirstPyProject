
# for x in range(3):
#     for y in range(1, 11):
#         print(y, end="")
#     print()

rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
symbol = input("Enter a symbol: ")

for x in range(rows):
    for y in range(cols):
        print(symbol, end="  ")
    print()
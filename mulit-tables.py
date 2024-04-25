num = int(input("enter a number"))
print("the multiplication table of:", num)
for count in range(1, 11):
    print(num, "X", count, "=", num * count)

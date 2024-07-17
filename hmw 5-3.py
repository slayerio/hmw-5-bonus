#1
while True:
    x = int(input("enter a number"))
    if x <= 0:
        print("put a positive number")
    else:
        break

for j in range(1, x+1):
    for i in range(1,j+1):
        print(i, end="")
    print()
for e in range(x, 0, -1):
    for c in range(1, e):
        print(c, end="")
    print()


#2
while True:
    y = int(input("enter a number"))
    if x <= 0:
        print("put an odd positive number")
    elif not x % 2:
        print("put an odd number")
    else:
        break

for a in range(1, y+1, 2):
    space = (y - a) // 2
    print(" " * space + '*' * a)
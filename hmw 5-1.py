positive = 0
negative = 0
zero = 0
module = 0
highest = 0
lowest = 0
for i in range(1,11):
    x = int(input("put a number"))
    if x == -9999:
        break
    if -1000 > x or x > 1000:
        continue
    if x > 0:
        positive += 1
        highest = x
    elif x < 0:
        negative += 1
        lowest = x
    else:
        zero += 1
    if not x % 7:
        module += 1
else:
    print(f"you put {negative} negative numbers, {positive} positive,"
          f" {zero} zero's, {module} numbers divided by 7 ")
    if highest:
        print(f"{highest} is the last positive number")
    else:
        print(f" there are no positive numbers")
    if lowest:
        print(f"{lowest} is the last negative number")
    else:
        print("there are no negative numbers")



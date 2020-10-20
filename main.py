a = int(input("Enter 1st number: "))
c = int(input("""1 - addition
2 - subtraction
3 - multipliaton
4 - division
> """))
b = int(input("Enter 2nd number: "))
if (c == 1):
    print ("addition result: ", a + b)
if (c == 2):
    print ("substraction result: ", a - b)
if (c == 3):
    print ("multipliation result: ", a * b)
if (c == 4):
    print ("division result: ", a / b)
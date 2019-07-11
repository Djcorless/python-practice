num = int(input("Enter a number:"))
if num % 4 == 0:
    print(num, "is a multiple of 4.")
elif num % 2 == 0:
    print(num, "is an even number.")
elif num % 2 != 0:
    print(num, "is an odd number.")
check = int(input("Enter another number:"))
if num % check == 0:
    print(check, "divides evenly into", num)
else:
    print(check, "doesn't divide evenly into", num)
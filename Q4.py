import math
num = input("Please enter a number:")
a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
b=[]
for i in range(1, 100):
    mul=int(num)/int(i)
    if int(num)%int(i)==0:
        b.append(mul)
        print(b)
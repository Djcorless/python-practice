a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a)
b= []
x = input("please enter a number listed above:")
for num in a[:]:
    if int(num)<int(x):
        b.append(num)
print(b) 
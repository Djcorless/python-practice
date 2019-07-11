import random
c = random.randrange(1, 9)
print(c)
q= input("pick a number between 1 to 9:")
if int(q)<int(c):
    print("your number was too low the number was", c)
elif int(q)>int(c):
    print("your number was too high the number was",c)
elif int(q)==int(c):
    print("you are correct!")
else:
    print("the number was I chose was", c)
    

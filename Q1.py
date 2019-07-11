name = input('What is your name?')
age = input('What is your age?')
b_day = input('have you had your birthday this year? Y/N')
yrsTil100 = 100 - int(age)
if b_day == "Y":
    uTurn100 = yrsTil100 + 2019
elif b_day == "N":
    uTurn100 = yrsTil100 + 2019 - 1
print('Neat! so ' + name + ' In the year ' + str(uTurn100) + " you'll be 100 years old!")
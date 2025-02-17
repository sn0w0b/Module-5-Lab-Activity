#Martha Moreno Gonzalez
#2/16/25
#identifies wheter an interger between 1-50 is divisible by 3 by 5 or by both

for i in range (1, 51):
    if i % 3 == 0 and i % 5 == 0 :
        print("Divisible by both")
    elif i % 3 == 0:
        print("divisible by three")
    elif i % 5 == 0:
        print("Divisible by five")
    else:
        print(i)



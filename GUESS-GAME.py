import random
n = random.randrange(100)
count = 0

while n!="guess":
    guess = int(input("enter the number \n" ))
    if count == 5:
        print("You lost")
        break

    if guess<n:
        print("Please enter the higher number")
    elif guess>n:
        print("Please enter the smaller number")
    else:
        print("You did it")

    count +=1



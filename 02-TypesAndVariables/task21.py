from random import randrange


dice = randrange(1 , 6)
guess = input("Enter a random number from 1 to 6: ")
guess = int(guess)

if dice == guess:
    print("True")
else:
    print("False")

print(f"The true answer is {dice}")
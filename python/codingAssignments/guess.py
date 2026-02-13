# Use math.log function to compute the
# minimum number of guesses needed  after the lower and upper
# bounds are entered
import random

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the large number:"))
myNumber = random.randint(smaller, larger)
count = 0
while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    else:
        print("Congratulations! You've got it in", count, "tries!")
        break


print(smaller, larger)

print("Your number is ")
print(input("Enter =, <, or >:"))

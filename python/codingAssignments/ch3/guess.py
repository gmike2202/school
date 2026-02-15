import math

# Get bounds
low = int(input("Enter the smaller number: "))
high = int(input("Enter the larger number: "))

# Compute maximum allowed guesses (minimum needed)
max_guesses = math.ceil(math.log(high - low + 1, 2))
guesses = 0

while guesses < max_guesses:
    print(low, high)
    guess = (low + high) // 2
    print("Your number is", guess)

    response = input("Enter =, <, or >: ")

    guesses += 1

    if response == "=":
        print(f"Hooray, I've got it in {guesses} tries!")
        break
    elif response == "<":
        high = guess - 1
    elif response == ">":
        low = guess + 1
    else:
        print("Invalid input.")
        guesses -= 1
        continue

    # Detect cheating (contradiction)
    if low > high:
        print("I'm out of guesses, and you cheated!")
        break

else:
    print("I'm out of guesses, and you cheated!")

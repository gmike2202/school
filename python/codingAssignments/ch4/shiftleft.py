# Maybe don't need to convert them to an integer,
# maybe can use string manipulation with subscripts
# to move them and wrap them around
bit_string = input("Enter a string of bits: ")

result = bit_string[1:] + bit_string[0]
print(result)

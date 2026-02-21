plainText = input("Enter a message: ")
distance = int(input("Enter the distance value: "))

code = ""

for ch in plainText:
    ordValue = ord(ch)
    cipherValue = (ordValue + distance) % 128

    code += chr(cipherValue)

print(code)

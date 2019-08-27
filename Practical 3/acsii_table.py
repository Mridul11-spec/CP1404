LOW_ASCII = 33
UP_ASCII = 127

print("Enter a number between 33 and 127")
value = int(input(">>>"))

while value < LOW_ASCII or value > UP_ASCII:
    print("Please chose the number from 33 to 127")
    value = int(input(">>>"))
    pass
result = (chr(value))
print("The character for", value, "is", result)



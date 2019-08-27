out_file = open('name.txt', 'w')
print ("Your name is Vincent", file=out_file)
out_file.close()

input_files = open('numbers.txt', 'r')
number1, number2 = input_files.readlines()
function = int(number1) + int(number2)
print(function)
input_files.close()



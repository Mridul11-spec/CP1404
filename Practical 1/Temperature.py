def main():
    menu= str(input("""C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
>>>"""))

    while menu !="Q" and menu != "q":
        if menu == "C" or menu == "c":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9/5 + 32
            print("Result: {:.2f} F".format(fahrenheit))
            menu = str(input("""C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
>>>"""))
        elif menu == "F" or menu == "f":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit * 5/9 - 32
            print("Result: {:.2f} C".format(celsius))
            menu = str(input("""C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
>>>"""))
        else:
            print('Invalid option')
            menu = str(input("C - Convert Celsius to Fahrenheit\n F - Convert Fahrenheit to Celsius\n Q - Quit\n >>> "))
    print("Thank You")

main()
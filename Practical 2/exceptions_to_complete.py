finished = False
result = 0
while not finished:
    try:
        salary = int(input("Enter your salary: "))
        month = int(input("How many days you have work in a month: "))
        result = salary / month
        print(result)
        pass
    except ZeroDivisionError :
        print("Cannot divide with zero number")
    except :
        print("Please enter a valid integer.")
print("Valid result is:", result)

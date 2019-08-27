sales = float(input("Enter sales: "))
if sales < 1000:
    discount = sales / 10
    print("User gets a 10% bonus")
    print("discount price = " , discount)
else:
    discount = sales / 15
    if discount <= 100:
        discount = 150
    if discount > 100 and discount <=200:
        discount = 300
    print("User gets a 15% bonus")
    print("discount price= " , discount)

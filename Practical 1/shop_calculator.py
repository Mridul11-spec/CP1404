def main():
    item_quantity = int(input("Number of Items: "))
    while item_quantity <= 0:
        print ("Invalid price")
        item_quantity = int(input("Number of Items: "))
    item_list = []
    for i in range (item_quantity):
        item_price = float(input("Price of Item: "))
        item_list.append(item_price)
        a = sum(item_list) / 10
    total_price = round (sum(item_list) - a , 2)
    print("Total Price for" ,  item_quantity, "items = $",total_price)
main()



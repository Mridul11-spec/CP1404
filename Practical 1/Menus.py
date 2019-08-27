def main():
    name = str(input('Enter Name: '))
    print('Hello ', name)
    menu = str(input('(H)ello\n(G)oodbye\n(Q)uit\n >>>'))
    while menu != "q" and menu != "Q":
        if menu == "h" and menu =="H":
            print ("Hello",name)
            menu = str(input('(H)ello\n(G)oodbye\n(Q)uit\n >>>'))
        elif menu == "G" and menu == "g":
            print ("Good bye",name)
            menu = str(input('(H)ello\n(G)oodbye\n(Q)uit\n >>>'))
        else:
            print('Invalid input')
            menu = str(input('(H)ello\n(G)oodbye\n(Q)uit\n >>>'))
    print("Finished")

main()
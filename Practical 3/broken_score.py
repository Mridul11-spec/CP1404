def main():
    score= float(input("Input your score:"))
    if score <101 and score >=100:
        print("Inclusive")
    elif score >= 90 and score <100:
        print ("Excelent")
    elif score >=50 and score <90:
        print ("Pass")
    elif score <50 and score >=0:
        print ("Bad")
    else:
        print("Invalid score")
main()
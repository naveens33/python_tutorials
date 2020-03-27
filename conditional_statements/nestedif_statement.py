if __name__=='__main__':
    age = int(input("Enter the age: "))
    if age >= 18:
        panstatus=input("Do you have pancard(yes/no): ")
        if panstatus == "yes":
            print("Eligible")
        else:
            print("Apply for pan")
    else:
        print("Not Eligible")
        
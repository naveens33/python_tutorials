li=[12,34,43]

while(True):
    index=int(input("enter the index: "))
    try:
        print(li[index])
    except Exception as err:
        print(err)
    finally:
        print("Thanks for using my code")

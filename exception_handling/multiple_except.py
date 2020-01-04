li=[12,34,43]

while(True):
    index=int(input("enter the index: "))
    try:
        print(li[index])
        c=7/0
    except IndexError as err:
        print("Hey, provide the valid index")
    except Exception as err:
        print(err)
    finally:
        print("Thanks for using my code")

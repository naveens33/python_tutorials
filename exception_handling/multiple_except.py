li = [12,43,54]

while True:
    try:
        index = int(input("Enter the index: "))
        x=9/0
        print(li[index])
    except IndexError as err:
        print("Hey provide valid index range")
    except ValueError as err:
        print("Hey provide valid index type")
    except Exception as err:
        print(err)
    finally:
        print("Thanks for using my code")
    stop = input("Do you want to stop(yes/no): ")
    if stop == 'yes':
        break
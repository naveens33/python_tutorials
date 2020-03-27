li = [12,43,54]

while True:
    index = int(input("Enter the index: "))
    try:
        print(li[index])
    except Exception as err:
        print(err)
    stop = input("Do you want to stop(yes/no): ")
    if stop == 'yes':
        break
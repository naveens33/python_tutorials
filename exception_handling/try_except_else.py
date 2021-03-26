try:
    b = int(input("Enter divisible number: "))
    c = 6/b
except Exception as err:
    print(err)
else:
    print("Don't without any exception")
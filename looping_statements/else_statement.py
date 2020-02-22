if __name__ == '__main__':
    '''
    i = 456
    while i < 1000:
        if i % 13 == 0 and i % 19 == 0:
            print(i)
            break
        i += 1
    else:
        print("No number found")
    '''
    for i in range(456,465):
        if i % 13 == 0 and i % 19 == 0:
            print(i)
            break
        i += 1
    else:
        print("No number found")
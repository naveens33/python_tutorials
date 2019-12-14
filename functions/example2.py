def removeduli(li):
    for i in li:
        count=li.count(i)
        if(count!=1):
            for j in range(1,count):
                li.remove(i)
    return li

if __name__=='__main__':
    li=[1,2,3,3,3,3,4,5,5]
    print(removeduli(li))

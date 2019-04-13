if __name__=='__main__':
    st="Process finished with exit code 0"
    count1=0
    count2=0
    for c in st:
        if(c.isupper()):
            count1=count1+1
        elif(c.islower()):
            count2=count2+1

    perupper=(count1/len(st))*100
    perlower=(count2/len(st))*100

    print(round(perupper,2))
    print(round(perlower,2))
#yield explanation
def simpleGeneratorFun():
    for i in range(10):
        yield i

for value in simpleGeneratorFun():
    print(value)

#find sum of odd number between 0-99
def generatedoddnumber():
    for i in range(0,100):
        if(i%2!=0):
            yield i

if __name__=='__main__':
    ans=0
    for oddnum in generatedoddnumber():
        ans=ans+oddnum
    print("sum of odd number: "+str(ans))
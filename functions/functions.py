#function example
def function1():
  print("Inside func1")

print('Outside func1')
function1()

#function-parameter example
def function2(para1,para2):
  print("Inside func2: "+str(5)+str(6))

print('Outside func2')
function2(5,6)

#example sum
def addition(para1,para2):
  print("answer: "+str(para1+para2))

addition(5,6)

#return statement
def return_example(para1):
    return(para1)

print(return_example("hi hello"))

#example- square
def square(para1):
    ans=para1*para1
    return(ans)

a=6
print("Square of {0} = {1} ".format(a,square(a)))

#default parameter
def default_para(Name = "Dhoni"):
  print("Player Name: " + Name)

default_para("Sachin")
default_para()

def findevennumbers(start,end):
    li=[]
    for i in range(start,end):
        if(i%2==0):
            li.append(i)
    return li

if __name__=='__main__':
    c=findevennumbers(80,98)
    print(c)


def total(m1,m2,m3,m4,m5):
    print("m1",m1)
    print("m2",m2)
    print("m3",m3)
    print("m4",m4)
    print("m5",m5)


mark=[12,34,54,65,54]
total(*mark)

def total(*mark):
    print(mark)
    print(sum(mark))

total(12,34,54,65,54)

def total(*mark,x):
    print(mark)
    print("x: ",x)
    print(sum(mark))

total(12,34,54,65,54,x=67)

def total(m1,m2,m3):
    print("m1",m1)
    print("m2",m2)
    print("m3",m3)

mark={"m1":32,"m2":43,"m3":100}
total(**mark)

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

#square
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

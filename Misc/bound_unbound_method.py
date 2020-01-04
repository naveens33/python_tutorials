#bound method
class Addition():
    num1=0
    num2=0
    def set_value(self, num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        sum=self.num1+self.num2
        print("sum: "+str(sum))

if __name__=='__main__':
    obj=Addition()
    obj.set_value(4,9)
    obj.add()

#unbound method
#interacts with classes only and not instances
#This can cause a future code maintenance problem
class Message():
    @staticmethod
    def display():
        print("This is bound method")

if __name__=='__main__':
    Message.display()

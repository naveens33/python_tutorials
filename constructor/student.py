class student:
    rollno=0
    feestatus=False

    def __init__(self,str):
        print(str)

    def display(self):
        print("World")

    def __del__(self):
        print("Destrutor")

if __name__=='__main__':
    s1=student("hello")
    del(s1)
    s2=student("hello2")

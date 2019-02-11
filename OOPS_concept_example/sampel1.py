class parent:
    __datamember1=0

    def memberfunc1(self):
        print(self.__datamember1)

class child(parent):
    datamember2=0

    def memberfunc2(self):
        print(self.datamember2)

if __name__=='__main__':
    obj2=child()
    obj2.datamember2=8
    obj2.memberfunc2()
    obj2.__datamember1=78
    obj2.memberfunc1()
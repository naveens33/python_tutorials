"""
def total(*args):
    z= sum(args)
    print(z)


total(54, 65, 34, 65, 34, 76, 34, 24)
"""


def total(m1, m2, m3, m4, m5):
    print(m1 + m2 + m3 + m4 + m5)


li = [65, 76, 98, 45, 76]
total(*li)


#*args (Variable length arugments), **kwargs(Variable length keyword arguments)
#keyword-only argument

def total(*m,noofsub):
    print(sum(m))
    print(noofsub)


total(12,43,54,65,67,noofsub=5)
total(56,45,87,noofsub=3)
total(56,45,87,56,noofsub=4)

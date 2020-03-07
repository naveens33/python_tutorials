def details(**kwargs):
    print(kwargs)


details(Name="Prem", Class=5, Rank=3, Address="Bangalore")

"""
def details(Name, Class, Rank, Address):
    print(Name, Class, Rank, Address)


d = {"Name": "Prem", "Class": 5, "Rank": 3, "Address": "Bangalore"}
details(**d)
"""

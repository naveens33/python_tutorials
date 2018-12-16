if __name__=="__main__":
    pass
'''
    #split
    names="adarsh,suresh,ramesh,kamal"
    splitans=names.split(',')
    print(splitans)
'''
'''
    #upper and lower
    name="Mr. Karthick"
    capital=name.upper()
    small=name.lower()
    print(capital)
    print(small)
'''
'''
    #find & index
    note = "Proof Of funds needs to be shown for the family and the friends"
    print(note.find("the"))
    print(note.index("the"))    
'''
'''
    #endswith
    name="Mr. Karthick BA. BL."
    if(name.endswith("BA. BL.")):
        print("Qualification Added")
'''
'''
    #startswith
    name="Mr. Karthick"
    if(name.startswith("Mr.")):
        print("Correct")
    else:
        print("Incorrect")
'''

'''
    #count
    note = "Proof Of funds needs to be shown for the family and the friends"
    #count=note.count("the")
    count=note.count("the",0,40)
    print(count)
'''
'''
    #replace
    note="Proof Of funds needs to be shown for the family"
    replacedstring=note.replace("family","friends")
    print(replacedstring)
'''
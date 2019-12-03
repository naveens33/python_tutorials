#String functions
if __name__=="__main__":
    #endswith
    name="Mr. Karthick BA. BL."
    if(name.endswith("BA. BL.")):
        print("Qualification Added")

    #split
    names="adarsh,suresh,ramesh,kamal"
    splitans=names.split(',')
    print(splitans)

    #upper and lower
    name="Mr. Karthick"
    capital=name.upper()
    small=name.lower()
    print(capital)
    print(small)

    #find & index
    note = "Proof Of funds needs to be shown for the family and the friends"
    print(note.find("the"))
    print(note.index("the"))    

    #startswith
    name="Mr. Karthick"
    if(name.startswith("Mr.")):
        print("Correct")
    else:
        print("Incorrect")

    #count
    note = "Proof Of funds needs to be shown for the family and the friends"
    print(note.count("funds"))

    #replace
    note="Proof Of funds needs to be shown for the family"
    replacedstring=note.replace("family","friends")
    print(replacedstring)

    #format
    name="he{}llo{}"
    print(name.format("3","5"))

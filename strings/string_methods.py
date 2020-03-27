# String functions
if __name__ == "__main__":
    # endswith
    name = "Mr. Karthick BA. BL."
    if (name.endswith("BA. BL.")):
        print("Qualification Added")

    # startswith
    name = "Mr. Karthick"
    if (name.startswith("Mr.")):
        print("Correct")
    else:
        print("Incorrect")

    # find & index
    # find vs index-> If the current substring is not there in the string
    # find will return -1 and index will throw exception (ValueError: substring not found)
    note = "Proof Of funds needs to be shown for the family and the friends"
    print(note.find("the"))
    print(note.index("the"))

    # count
    note = "Proof Of funds needs to be shown for the family and the friends"
    print(note.count("funds"))

    # upper and lower
    name = "Mr. Karthick"
    capital = name.upper()
    small = name.lower()
    print(capital)
    print(small)

    # replace
    # count in replace is provided to say how many substring to be replaced
    note = "Proof Of funds needs to be shown for the family and the friends"
    replacedstring = note.replace("the", "hello")
    print(replacedstring)
    replacedstring = note.replace("the", "hello",1)
    print(replacedstring)

    # format
    sentence = "{} is coming from {}"
    print(sentence.format("Prem", "Bangalore"))
    print(sentence.format("Somi", "Delhi"))

    # split
    names = "adarsh,suresh,ramesh,kamal"
    splitans = names.split(',')
    print(splitans)

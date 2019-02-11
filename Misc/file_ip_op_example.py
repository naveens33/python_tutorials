#Read I/P from console window
fname = input("Enter your name: ")
print ("First Name : ", fname)

# Open a file and mode definition
fo = open("outputfile.txt", "w")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()

# Open a file and write
fo = open("outputfile.txt", "w")
fo.write( "Writing into file.\nMove Forward!!\n");
fo.close()

# Open a file and append
fo = open("outputfile.txt", "a")
fo.write( "Appending into file.\nGreat Day!!\n");
fo.close()

# Open file and read file
fi=open("inputfile.txt","r")
print(fi.read())
#print(fi.read(5))
#print(fi.readline())


#delete file
#import os
#os.remove("outputfile.txt")
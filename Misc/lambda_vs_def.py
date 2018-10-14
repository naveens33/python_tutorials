sum=lambda x,y:x+y

print(sum(5,6))

#def sum(x,y)
#   return(x+y)

my_list=[1,25,3,76,89]

newlist=list(filter(lambda x:(x%2==0),my_list))
print(newlist)
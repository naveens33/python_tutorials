price = [13.44,1056.50, 940.00, 22.00]
def get_price_with_gst(amount):
    return round(amount + ((amount/100)*18),2)
total_price = map(get_price_with_gst,price)
print(list(total_price))


#Convert a list of float to int using map
li = [13.44,1056.50, 940.00, 22.00]
print(list(map(int,li)))
'''
The above statement is equivalent to 
ans=[]
for i in li:
    ans.append(int(i))
print(ans)
'''
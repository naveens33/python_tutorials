#calculate.py
import total,average
m1=150
m2=156
m3=176
m4=200
m5=187
ans_total=total.gettotal(m1,m2,m3,m4,m5)
ans_average=average.getaverage(ans_total,5)
print("Total: "+str(ans_total))
print("Average: "+str(ans_average))
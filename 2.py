l=[]
for i in range(0, 1000):
    if (i%7==0) and (i%4!=0):
        l.append(str(i))
 
print (','.join(l))

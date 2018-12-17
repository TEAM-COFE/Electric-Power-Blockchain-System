def fun1(x1):
    global b  
    if x1>0:
        a=x1
        b=a
        print ('b[0]==',b)
        return a
    else:
        ccc=b
        print ('ccc===',ccc)
        return  ccc   

z=fun1(0)
print ('z==',z)
y=fun1(1)
print ('y==',y) 
z=fun1(0)
print ('z==',z)
 
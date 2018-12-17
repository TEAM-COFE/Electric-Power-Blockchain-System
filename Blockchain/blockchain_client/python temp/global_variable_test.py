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
def fun2(x2):
    global b  
    if x2>0:
        a2=x2
        b2=a2
        print ('b[0]==',b2)
        return a2
    else:
        ccc2=b2
        print ('ccc===',ccc2)
        return  ccc2  
    
#z=fun1(0)
#print ('z==',z)
y=fun1(1)
print ('y==',y) 
z=fun1(0)
print ('z==',z)
def test():
    y2=fun2(1)
    print ('y2==',y2)
    return y2
uu=test()
print ('uu==',uu)
ww=test()
print ('uu==',uu)    
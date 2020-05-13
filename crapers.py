L=map(int,raw_input().strip().split())

n=L.pop(0)
a=min(L)
b=max(L)

def fun(n,a,b):
    s=b

if(n<a):
    print "NO"
elif(n==a):
    print "YES"
    print a
elif(n<=b):
    print "YES"
    print n,
elif(n<=b+a):
    print "YES"
    print a,
    print n-a,
else:
    print "YES"
    remain=n%b
    number=n//b
    if(remain==0):
        for i in range(number):
            print b,
    elif(remain<a):
        remain+=b
        if (remain<=b):
            if (remain<=b*2):
                print 
            for i in range(number-1):
                print b,
    elif(a<=remain<b):
        print remain,
        for i in range(number):
            print b,
            
    
    

            

            


        
        
    

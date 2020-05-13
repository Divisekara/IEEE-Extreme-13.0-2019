import itertools 

t=int(raw_input().strip())

def alpha(n):
    return chr(n+97)

for a in range(t):
    
    n,m=map(int,raw_input().strip().split())
    if (n==1 or m==0):
        print "a"
        continue
    count=0
    while(m>0):
        new=m-(n**count)*count
        if(new<0):
            break
        else:
            m=new
        count+=1

    if(m<=0):
        print "a"
        continue
    L=[]
    for i in range(n):
        L.append(alpha(i))

    for i in list(itertools.product(L, repeat=count)):
        if (m<count):
            print list(i)[m]
            break
        m=m-count
        
        
    


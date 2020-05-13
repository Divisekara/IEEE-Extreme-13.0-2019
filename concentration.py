import sys
n=int(raw_input().strip())

for i range(1,2*n+1):
    L.append(i)

print 1,2
put=[1,2]



while(True):
    a,b=map(int,raw_input().strip().split())
    put+=[a]
    put+=[b]
    if(put.count(a)==1):
        print a,
    if(put.count(b)==1):
        print b
    
    
    
    
    

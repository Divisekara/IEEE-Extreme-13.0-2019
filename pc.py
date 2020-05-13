t=int(raw_input())

import itertools

for a in range(t):
    try:
        budget=int(raw_input())
        comps=int(raw_input())
        L=[]
        
        options=map(int,raw_input().strip().split())
        
        for b in range(comps):
            L_=map(int,raw_input().strip().split())
            L.append(L_)
            
        while(len(L)>1):
            L1=L[0]
            L2=L[1]
            L3=[]
            for i in L1:
                for j in L2:
                    if((i+j)<=budget):
                        L3.append(i+j)
                    
            L.pop(0)
            L.pop(0)
            L.append(L3)
            
    ##'''
    ##    L4=[]
    ##    for z in L3:
    ##        if (z<=budget):
    ##            L4.append(z)
    ##'''
            
        print max(L3)
    except:
        print 0
        

        

    


    
        
    


    

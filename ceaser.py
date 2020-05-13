def isLex(L):
    
    m=(len(L)+1)//2
    left=L[0:m]
    right=L[m:]

    if(m==0 or m==1):
        return True
    elif(left<=right and m>0):
        return (isLex(left) and isLex(right))
    else:
        return False



n=int(raw_input().strip())

display=''

for i in range(n):
    
    L=list(raw_input())
    if (len(list(set(L)))==1):
        display+='1'
        continue
    else:
        M="".join(L)
        if(isLex(M)):
            display+="1"
            
        else:
            display+='0'


print display
            
            
        
        

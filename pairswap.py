n=int(raw_input())

def swap(L,check):
    
    temp=L[:]
    pos1=L.index(check)
    temp.remove(check)
    pos2 = temp.index(check)
    L[pos1], L[pos2] = L[pos2], L[pos1] 
    return L

for i in range(n):
    word=list(raw_input().strip())
    L=word[:]
    m = len(word)

    i=0
    while(i<m-1):
        check = word[i]
        pre = word[i-1]
        nex = word[i+1]
        if (check!=nex and word.count(check)>1):
            temp=swap(word,check)
            word=temp[:]
        else:
            i+=1
        i+=1

    print ("".join(map(str,word)))
    
        
            
    

    
    

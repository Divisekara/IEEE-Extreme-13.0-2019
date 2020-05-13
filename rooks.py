n,m=map(int,raw_input().strip().split())

A=map(int,raw_input().strip().split())
S=list(map(int,raw_input().strip().split()))

S.sort()

i=0

for j in S:
    for k in range(i,n):
        if (j<A[k]):
            print j,
            break
        else:
            print A[k],
            i+=1
    else:
        display=" ".join(map(str,S[S.index(j):]))
        print display,
        break 
else:
    display=" ".join(map(str,A[k:]))
    print display,        


    

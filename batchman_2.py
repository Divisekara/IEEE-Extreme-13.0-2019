def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

n,m=map(int,raw_input().strip().split())
L=map(int,raw_input().strip().split())

answers=[]

minimum=min(L)
maximum=max(L)

count=0

for i in range(maximum,minimum,-1):
    if (i in L):
        answers.append(i)
        count+=1
    else:
        g=gcd(L[count-1],L[count])
        if(g not in answers):
            answers.append(g)

print len(answers)

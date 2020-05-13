n,m=map(int,raw_input().strip().split())

lines=[]
for j in range(m):
    lines.append(raw_input().strip())    

L=[]
for i in range(n):
    L.append(chr(65+i))
    

row=''
traingle=n*(n-1)/2

alls=[]

for a in range(0,n):
    for b in range(a,n):
        

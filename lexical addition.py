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
    print n
elif(n>b):
    if((n-a)<a):
        print "NO"
    else:
        print "YES"
        number=n//b  #2
        remain = n%b #2
        if (remain>=a):
            print remain,
            for i in range(number):
                print b,
        else:
            if (remain!=0):
                remain += b
                
                print min(remain-a,a),
                
                print max(remain-a,a),
                for i in range(number-1):
                    print b,
            else:
                for i in range(number):
                    print b,

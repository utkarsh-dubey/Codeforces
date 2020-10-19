t=int(input())

for T in range(t):

    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    amin=min(a)
    bmin=min(b)
    count=0
    for i in range(n):
        count+=max(a[i]-amin,b[i]-bmin)

    print(count)


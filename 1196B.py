t=int(input())

for T in range(t):

    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    o=[]
    for i in range(n):
        if(a[i]%2!=0):
            o.append(i+1)

    if(len(o)>=k and (len(o)-k)%2==0):
        print("YES")
        for j in range(k-1):
            print(o[j],end=" ")
        print(n)
    else:
        print("NO")



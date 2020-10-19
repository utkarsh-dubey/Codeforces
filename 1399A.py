t=int(input())

for T in range(t):

    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    flag=0
    for i in range(n-1):
        if(abs(a[i]-a[i+1])>1):
            print("NO")
            flag=1

            break
    if(flag==0):
        print("YES")
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort();
if(k>len(a)):
    print(-1)
    exit()
if(k==0):
    if(a[0]>1):
        print(a[0]-1)
    else:
        print(-1)

    exit()
if(len(a)==k):
    print(a[k-1])
    exit()

if(a[k-1]!=a[k]):
    print(a[k-1])
else:
    print(-1)



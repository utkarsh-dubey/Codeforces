n,l=map(int,input().split())

a=list(map(int,input().split()))

a.sort()

ans=0

for i in range(n-1):

    ans=max(ans,abs(a[i]-a[i+1]))

if(a[0]==0 and a[n-1]==l):
    print(ans/2)
else:
    print(max(a[0],ans/2,l-a[n-1]))
n=int(input())
a=list(map(int,input().split()))

a.sort()
if(n%2==0):
    print(a[n//2-1])
else:
    print(a[n//2])

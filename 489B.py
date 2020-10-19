from math import inf


n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

a.sort()
b.sort()
# print(a)
# print(b)
ans=0
for i in range(n):
    for j in range(m):
        if(abs(a[i]-b[j])<=1):
            ans+=1
            b[j]=inf
            break


print(ans)
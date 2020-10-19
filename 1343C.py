t=int(input())
from math import inf
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))


    i=0
    num=-1
    sums=[]
    while(i<n):
        j=i+1
        num+=1
        sums.append([a[i]])
        while(j<n and ((a[i]>0 and a[j]>0) or (a[i]<0 and a[j]<0))):
            sums[num].append(a[j])
            j+=1

        i=j
    sum=0
    for i in sums:
        sum+=max(i)


    print(sum)

from copy import deepcopy
from math import inf


t=int(input())
for T in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    for i in range(2,2*n+1):
        temp=0
        # b=deepcopy(a)
        hashy={}
        for j in range(n):
            if(a[j] in hashy):
                hashy[a[j]]+=1
            else:
                hashy[a[j]]=1
        for j in range(n):
            if(hashy[a[j]]>0):
                if(i-a[j] in hashy and ((hashy[i-a[j]]>0 and a[j]!=i-a[j]) or (hashy[i-a[j]]>1 and a[j]==i-a[j]))):
                    temp+=1
                    hashy[a[j]]-=1
                    hashy[i-a[j]]-=1

            # for k in range(j+1,n):
            #     if(b[j]+b[k]==i):
            #         temp+=1
            #         b[k]=inf
            #         break
        # print(i,temp)
        count=max(count,temp)

    print(count)
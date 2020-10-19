from math import *
n,k=map(int,input().split())
check=[]
for i in range(26):
   check.append(chr(i+97))

ans=""
count=0
for i in range(n//k):
    for j in range(k):
        ans+=check[j]
        print(check[j],end="")
        count+=1

for i in range(n%k):
    if(ans[-1]!='a'):
        print(check[i],end="")
    else:
        print(check[i+1],end="")


n=int(input())
a=list(map(int,input().split()))
count=0
a.sort()
num=1
for i in range(len(a)):
    if(a[i]>=num):
        count+=1
        num+=1

print(count)
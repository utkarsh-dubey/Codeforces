n=int(input())
b=list(map(int,input().split()))

a=[]
num=0
for i in range(0,n):
    if(i==0):
        a.append(b[i])
        num=b[i]
    else:

        a.append(b[i]+num)
        num=max(num,a[i])


for i in range(n):
    print(a[i],end=" ")
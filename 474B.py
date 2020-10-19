
def sear(a,low,high,num):
    mid=(low+high)//2
    if(num <= ans[mid] and num > ans[mid - 1]):
        return mid
    elif(num>ans[mid]):
        return sear(a,mid+1,high,num)
    else:
        return sear(a,low,mid-1,num)



n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

ans=[]
temp=0
for i in range(n):
    ans.append(a[i]+temp)
    temp=ans[i]

for i in range(m):

    if(b[i]<=ans[0]):
        print(1)
        continue
    print(sear(a,1,n,b[i])+1)

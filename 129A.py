n=int(input())
a=list(map(int,input().split()))

num=0
num1=0

sum=0

for i in a:
    sum+=i
    if(i%2==0):
        num+=1
    else:
        num1+=1

if(sum%2==0):
    print(num)
else:
    print(num1)
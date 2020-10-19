n=int(input())
s=str(input())

all=[]

for i in range(n-1):

    all.append(s[i:i+2])

ans=" "
number=0

for i in all:

    if(number<all.count(i)):
        ans=i;
        number=all.count(i)

print(ans)
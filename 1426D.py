n=int(input())

a=list(map(int,input().split()))

sums=set([0])
sum=0
count=0
for i in a:

    sum+=i
    if sum in sums:

        count+=1
        sums=set([0])
        sum=i

    sums.add(sum)

print(count)



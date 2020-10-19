n=int(input())
a=list(map(int,input().split()))
ans=0

for i in range(n):
    for j in range(i,n):
        ans=max(ans,a[i:j+1].count(0)+a[:i].count(1)+a[j+1:].count(1))
        # print("ans", ans ,"i",i,"j",j)

print(ans)

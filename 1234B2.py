from collections import deque

n,k=map(int,input().split())
a=list(map(int,input().split()))
# if(k>=n):
#     for i in a:
#         print(i,end=" ")
#         exit(0)

ans=deque([]);
check={}

for i in a:
    if i not in check and len(ans)==k:
            temp=ans.pop();
            ans.appendleft(i)
            check.pop(temp)
            check[i]=1
    elif i not in check:
        ans.appendleft(i)
        check[i]=1

print(len(ans))
for i in ans:
    print(i,end=" ")







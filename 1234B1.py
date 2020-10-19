from collections import deque

n,k=map(int,input().split())
a=list(map(int,input().split()))
# if(k>=n):
#     for i in a:
#         print(i,end=" ")
#         exit(0)

ans=deque([]);


for i in a:
    if i not in ans and len(ans)==k:
            ans.pop();
            ans.appendleft(i)
    elif i not in ans:
        ans.appendleft(i)

print(len(ans))
for i in ans:
    print(i,end=" ")







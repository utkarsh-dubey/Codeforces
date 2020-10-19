from collections import deque





n=int(input())
a=list(map(int,input().split()))

ans=deque([a[0]]);
prev=a[0]
a.remove(prev)
while(len(ans)!=n):

    num=prev
    prevone=0
    prevtwo=0
    nextone=0
    nexttwo=0
    if(num%3==0):
        nextone=num/3;
        nexttwo=num*2
    else:
        nextone=-1
        nexttwo=num*2

    if(num%2==0):
        prevone=num/2
        prevtwo=num*3
    else:
        prevone=-1
        prevtwo=num*3


    if nextone in a:
        ans.append(int(nextone))
        a.remove(nextone)
        prev=nextone
    elif nexttwo in a:
        ans.append(int(nexttwo))
        a.remove(nexttwo)
        prev=nexttwo
    elif prevone in a:
        ans.appendleft(int(prevone))
        a.remove(prevone)
        prev=prevone
    elif prevtwo in a:
        ans.appendleft(int(prevtwo))
        a.remove(prevtwo)
        prev=prevtwo
    elif(len(ans)!=1):
        prev=ans[0]
    else:
        prev=a[0]
        a.append(ans[0])
        ans=deque([a[0]])
        a.remove(prev)





for i in ans:
    print(i,end=" ")


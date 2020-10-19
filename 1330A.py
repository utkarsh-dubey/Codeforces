
def disp(a):
    for i in range(len(a)):
        print(a[i],end=' ')

    print()


t=int(input())

for i in range(t):
    n,x=map(int,input().split())
    # print(x)
    a=set(map(int,input().split()))
    a=list(a)
    a=sorted(a)
    length=len(a)
    # print(length)
    v=0
    # disp(a)
    num=0
    k=1;
    # disp(a)
    while(True):
        # print(k)
        if(num<length and a[num]==k):
            # print(num)
            num+=1
            k+=1
            # print(a[k])
            v+=1
        elif(x>0):
            k+=1
            # print(x)
            x-=1
            v+=1
        elif(x<=0):
            break
    print(v)
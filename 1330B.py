def disp(a):
    for i in range(len(a)):
        print(a[i],end=" ")

    print()

t=int(input())

for k in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    setf=set(a)
    count=0
    ans=[[]]
    eh=max(a)
    # he=min(a)
    # print(eh)
    # print(he)
    he=len(a)-len(setf)
    # print(he)
    for i in range(1,n):
        # print(i)
        if(i!=eh and i!=he):
            continue
        temp=a[:i]

        # print(len(temp))
        temp2=a[i:]
        # print(len(temp2))


        set1=set(temp)
        set2=set(temp2)
        if(len(set1)!=len(temp) or len(set2)!=len(temp2)):
            continue
        # temp.sort()
        # temp2.sort()
        if(max(temp)==i and max(temp2)==n-i):
            count+=1
            # disp(temp)
            # disp(temp2)
            # b=list(len(temp),len(temp2))
            ans.append([len(temp),len(temp2)])

    print(count)
    num=0
    for i in ans:
        if(num>0):
            print(i[0],end=" ")
            print(i[1])

        num+=1

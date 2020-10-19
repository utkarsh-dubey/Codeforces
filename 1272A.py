n = int(input())

for i in range(n):

    a, b, c = map(int, input().split())

    lis = [a, b, c]
    lis.sort()
    dist = 0
    flag = 0
    if(lis[0]-lis[1]==0 and lis[1]-lis[2]==0):
        print(dist)
        continue
    if (abs(lis[0] - lis[1] != 0)):
        dist = abs(lis[0] - lis[1]) - 1
        lis[0] += 1
    else:
        lis[0] += 1
        lis[1] += 1
        flag = 1
    if (abs(lis[1] - lis[2] != 0)):
        dist = dist + abs(lis[1] - lis[2]) - 1
        lis[2] -= 1
    elif (flag == 0):
        dist-=1
        lis[2] -= 1

    dist += abs(lis[0] - lis[2])

    print(dist)

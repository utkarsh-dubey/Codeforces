d=['ABSINTH', "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", "TEQUILA", 'VODKA', "WHISKEY", "WINE"]
for i in range(18):
    d.append(str(i))


n=int(input())
ans=0
for _ in range(n):
    s=input()
    if(s in d):
        ans+=1


print(ans)
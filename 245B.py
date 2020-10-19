s=str(input())
ans=""
check=False
check2=False
for i in range(len(s)):
    if(s[i]=='p' and not check):
        ans+='p://'
        check=True
        continue

    if(s[i-1]=='r' and s[i]=='u' and not check2 and ans[-2]!='/'):
        if(i!=len(s)-1):
            ans=ans[:-1]+".ru/"
        else:
            ans = ans[:-1] + ".ru"

        check2=True
        continue
    # print(ans)
    ans+=s[i]

print(ans)


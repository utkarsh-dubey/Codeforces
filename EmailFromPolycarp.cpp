#include<iostream>
#include<vector>
#include<stack>
#include<algorithm>
#include<string>
#define loop(i,ct,n) for(int i=ct;i<n;i++)
using namespace std;
string st, st2;
void solve()
{
    cin>>st;
    cin>>st2;
    int l=st.length(),ll=st2.length();
    if(l<=ll)
    { 
        stack <char> ss;
        int q=0;
        loop(i,0,l)
        {
            if(q<ll && st[i]==st2[q])
            {
                q++;
                while(!ss.empty())ss.pop();
                while(q<ll && st[i]==st2[q])
                {
                    ss.push(st[i]);
                    q++;
                }
            }else{
                if(!ss.empty() && st[i]==ss.top()) ss.pop();
                else{   
                    cout<<"NO"<<endl;
                    return;
                }
            }
        }
        if(q<ll) cout<<"NO"<<endl;
        else cout<<"YES"<<endl;
    }else cout<<"NO"<<endl;
}
int main()
{
   int t;
   cin>>t;
   while(t--) solve();
   return 0;
}
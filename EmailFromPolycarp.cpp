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
    char prc;
    loop(i,0,l)
    {
      if(st[i]==st2[q] && q<ll)
      {
        q++;
        loop(j,q,ll)
        {
          if(st[i]==st2[j])
          {
            ss.push(st[i]);q++;
            if (q>=ll) break;
            
          }
          else break;
        }
      }else
      {
        if(!ss.empty())
        {
          if(st[i]==ss.top()) {ss.pop();}
          else
          {
            while(!ss.empty()) ss.pop();
            cout<<"NO"<<endl;
            return; 
          }
        }else
        {
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
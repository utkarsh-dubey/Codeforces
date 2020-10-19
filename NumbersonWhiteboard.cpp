#include <bits/stdc++.h>
 
using namespace std;
 
#define ar array
#define ll long long
 
const int MAX_N = 1e5 + 1;
const int MOD = 1e9 + 7;
const int INF = 1e9;
const ll LINF = 1e18;
 
 
 
void solve() {
    int n;
    cin>>n;
    if(n==2)
    {
        cout<<2<<endl;
        cout<<"1 2"<<endl;
    }
    else
    {
        cout<<2<<endl;
        int num;
        for(int i=n-1;i>0;i--)
        {
            if(i==n-1)
            {
                cout<<n<<" "<<n-2<<endl;   
                num=n-1;
            }
            else if(i==n-2)
            {
                cout<<n-1<<" "<<n-1<<endl;
                num=n-1;
            }
            else
            {
                cout<<i<<" "<<num<<endl;
                num=(i+num)/2;
                
            }         
        }
    }
    // cout<<"\n";
}
 
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
 
    int tc; cin >> tc;
    for (int t = 1; t <= tc; t++) {
        solve();
    }
}
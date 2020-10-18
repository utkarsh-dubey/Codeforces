#include <bits/stdc++.h>
    
    using namespace std;
    
    #define ar array
    #define ll long long
    
    const int MAX_N = 1e5 + 1;
    const int MOD = 1e9 + 7;
    const int INF = 1e9;
    const ll LINF = 1e18;
    
    
    
    void solve() {
        ll n;
        cin>>n;
        ll sum=0;
        while(n!=0)
        {
            // cout<<n;
            if(n%2==0)
            {
                if(n%4==0 && n!=4)
                {
                    sum++;
                    n--;
                }
                else
                {
                sum+=n/2;
                n=n/2;
                }
            }
            else
            {
                sum++;
                n--;
            }
            if(n!=0)
            if(n%2==0)
            {
               
                if(n%4==0 && n!=4)
                {
                    n--;
                }
                else
                {
                    n=n/2;
                }   
            }
            else
            {
                n--;
            }
            
 
 
        }
        cout<<sum;
        cout<<"\n";
    }
    
    int main() {
        ios_base::sync_with_stdio(0);
        // #ifndef ONLINE_JUDGE
        // freopen("input.txt", "r", stdin);
        // freopen("error.txt", "w", stderr);
        // freopen("output.txt", "w", stdout);
        // #endif
        cin.tie(0); cout.tie(0);
    
        int tc; cin >> tc;
        for (int t = 1; t <= tc; t++) {
            solve();
        }
    }

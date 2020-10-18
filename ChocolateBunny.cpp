#include <bits/stdc++.h>
#include<string.h>
using namespace std;
 
#define ar array
#define ll long long
 
const int MAX_N = 1e5 + 1;
const int MOD = 1e9 + 7;
const int INF = 1e9;
const ll LINF = 1e18;
 
 
 
void solve() {
    
    
    cout<<"\n";
}
 
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
 
    int tc; cin >> tc;
    int A[tc]={0};
    int in=1;
    for(int i=2;i<=tc;i++)
    {
        string gg="? "+to_string(in)+" "+to_string(i)+"\n";
        cout<<gg;
        cout.flush();
        int g,h;
        cin>>g;
        string hh="? "+to_string(i)+" "+to_string(in)+"\n";
        cout<<hh;
        cout.flush();
        cin>>h;
        if(h>g)
            A[i-1]=h;
        else
        {
            A[in-1]=g;
            in=i;
        }
    }
    A[in-1]=tc;
    cout<<"! ";
    for(int i=0;i<tc;i++)
        cout<<A[i]<<" ";
    }
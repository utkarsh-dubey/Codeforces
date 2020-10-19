//utkarsh dubey 

#include<iostream>
#include<string.h>
#include<ctype.h>
#include<cstring>
#include<iomanip>
#include<cstdlib>
#include<vector>
#include<unordered_map>
#include<unordered_set>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<set>
#include<utility>
#include<algorithm>
 
using namespace std;
#define fastio() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define pb push_back
typedef long long ll;
#define fo(i,n) for(int i=0;i<n;i++)
bool rev(ll a, ll b) {return a > b;}
void swap(int &x, int &y) {int temp = x; x = y; y = temp;}
 
int main()
{
    
fastio();
    int t;
    cin>>t;
    vector<ll> a;
    vector<ll> b;

    fo(i,t){
        ll temp;
        cin>>temp;
        a.pb(temp*(i+1)*(t-i));

    }
    fo(i,t){
        ll temp;
        cin>>temp;
        b.pb(temp);
    }
    
    sort(a.begin(),a.end());
    sort(b.begin(),b.end(),rev);
    // for(int i:a){
    //     cout<<i<<" ";
    // }
    // cout<<endl;

    // for(int i:b){
    //     cout<<i<<" ";
    // }
    // cout<<endl;
    ll ans=0;
    fo(i,t){
        
        ans=(ans+((a[i]%998244353)*b[i])%998244353)%998244353;
        // cout<<ans<<endl;
        // ans%=998244353;
        


    }

    cout<<ans<<endl;


 
    return 0;
    
}
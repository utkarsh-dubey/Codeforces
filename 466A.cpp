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
 #include<cmath>
using namespace std;
#define fastio() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define pb push_back
typedef long long ll;
#define fo(i,n) for(int i=0;i<n;i++)
bool rev(int a, int b) {return a > b;}
void swap(int &x, int &y) {int temp = x; x = y; y = temp;}
 
int main()
{
    
fastio();
    float n,m,a,b;
    cin>>n>>m>>a>>b;
    
    if(b/m>a){
        cout<<n*a;
        
    }
    else{
        int sum1=int(n/m)*b+(int(n)%int(m))*a;
        int sum2=(int(n/m)+1)*b;
        if(sum2<sum1){
            cout<<sum2;

        }
        
        else{
            cout<<sum1;
        }
        
    }
    
}
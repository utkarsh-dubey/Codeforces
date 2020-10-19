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
bool rev(int a, int b) {return a > b;}
void swap(int &x, int &y) {int temp = x; x = y; y = temp;}
 
int main()
{
    
fastio();
    int t;
    cin>>t;

    while(t--){

        ll n;
        cin>>n;
        int count=0;
        while(n>=1){
            if(n%5==0){
                n=(4*n)/5;
                count++;
                continue;
            }
            if(n%3==0){
                n=(2*n)/3;
                count++;
                continue;
            }
            if(n%2==0){
                n=n/2;
                count++;
                continue;
            }
            break;
        }
        if(n==1){
            cout<<count<<endl;

        }
        else{
            cout<<"-1"<<endl;
        }

    }
 
    return 0;
    
}
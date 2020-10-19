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

bool check(int a[2][2]){
    
    int temp[2][2];
    fo(i,2){
        fo(j,2){
            temp[i][j]=a[j][i];
        }
    }

    if(a[0][1]==temp[0][1]&&a[1][0]==temp[1][0]){
        return true;
    }

    return false;
}

int main()
{
    
fastio();
    int t;
    cin>>t;

    while(t--){
        int n,m;
        int once=0;
        cin>>n>>m;
        if(m%2!=0){
            cout<<"NO"<<"\n";
            once=1;
            

        }
        int a[2][2];
        
        fo(i,n){
            cin>>a[0][0]>>a[0][1];
            cin>>a[1][0]>>a[1][1];  
            if(check(a)&&once==0){
                cout<<"YES"<<"\n";
                once=1;
            }
        }
        if(once==0){
            cout<<"NO"<<"\n";
        }



    }
 
    return 0;
    
}
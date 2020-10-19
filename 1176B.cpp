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
        int n;
        cin>>n;
        int count=0;
        int a[n];
        vector<int> num;
        int one=0;
        int two=0;
        
        fo(i,n){
            cin>>a[i];
            if(a[i]%3==0){
                count++;
            }
            else if(a[i]%3==1){
                one++;
            }
            else{
                two++;
            }
        }
        // cout<<one<<" "<<two<<endl;
        if(one<=two){
            count+=one;
            two-=one;
            if(two>=3){
                count+=two/3;
            }
        }
        else{
            count+=two;
            one-=two;
            if(one>=0){
                count+=one/3;
            }
        }

        cout<<count<<endl;

    }
 
    return 0;
    
}
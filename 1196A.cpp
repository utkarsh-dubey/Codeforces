#include<iostream>
#include<string.h>
#include<ctype.h>
#include<cstring>
#include<iomanip>
#include<cstdlib>
#include<set>
#include<utility>
#include<algorithm>
 
typedef long long ll;
 
using namespace std;
 
int main()
{
    
    int t;
    cin>>t;

    while(t--){

        ll a,b,c;
        cin>>a>>b>>c;
        ll total=a+b+c;
        if(total%2==0){
            cout<<total/2<<endl;

        }
        else{
            cout<<(total-1)/2<<endl;

        }




    }
 
    return 0;
    
}
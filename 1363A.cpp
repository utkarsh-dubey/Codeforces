    //utkarsh dubey 

    #include <bits/stdc++.h>
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
    #include<math.h>
    
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

            int n,x;
            cin>>n>>x;
            int a[n];
            int odd=0,even=0;
            for(int i=0;i<n;i++){
                cin>>a[i];
                if(a[i]%2==0){
                    even++;
                }
                else{
                    odd++;
                }
            }
            
            if(odd==0 || (odd==n && x%2==0) ||(x==n && odd%2==0)){
                cout<<"No\n";
                continue;
            }
            // if(x==n){
            //     if(odd%2==0){
            //         cout<<"No\n";
            //     }
            //     else{
            //         cout<<"Yes\n";
            //     }
            //     continue;
            // }
            // if(odd==n && x%2==0){
            //     cout<<"No\n";
            //     continue;
            // }
            cout<<"Yes\n";

            

        }
        
    
        return 0;
        
    }
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
    int n;
    cin>>n;

    if(n>21){
        cout<<0;
        return 0;
        
    }
    if((n>10 && n<20) || n==21 ){
        cout<<4;
        return 0;
    }
    if(n==20){
        cout<<15;
        return 0;
    }
    if(n<=10){
        cout<<0;
        return 0;
    }
    
 
    return 0;
    
}
//utkarsh dubey

#include <bits/stdc++.h>
#include <iostream>
#include <string.h>
#include <ctype.h>
#include <cstring>
#include <iomanip>
#include <cstdlib>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <utility>
#include <algorithm>
#include <math.h>

using namespace std;
#define fastio()                      \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL)
#define pb push_back
typedef long long ll;
#define fo(i, n) for (int i = 0; i < n; i++)
bool rev(int a, int b)
{
    return a > b;
}
void swap(int &x, int &y)
{
    int temp = x;
    x = y;
    y = temp;
}

int main()
{

    fastio();
    int t;
    cin >> t;

    while (t--)
    {

        int n;
        cin >> n;

        int num = floor(pow(n, 0.5));
        int finalnum = (n / num) + (num - 1);
        // cout<<"check1"<<num<<"\n";
        // cout<<"check"<<finalnum<<"\n";
        int dekhte = n / num;
        // cout<<"jada hai "<<n;
        // cout<<"\n";
        // cout<<"ek min"<<dekhte<<"\n";
        // if(num==1){
        //     cout<<"0"<<"\n";
        //     continue;
        // }
        if (n % (num) == 0)
        {
            cout << finalnum - 1 << "\n";
        }
        else
        {
            cout << finalnum << "\n";
        }
    }

    return 0;
}
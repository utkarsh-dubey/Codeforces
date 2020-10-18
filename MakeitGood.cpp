#include <iostream>
using namespace std;
 
int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
	    int n;
	    cin>>n;
	    int a[n];
	    int r=0;
	    for(int j=0;j<n;j++)
	    cin>>a[j];
	    for(int j=n-1;j>=0;j--)
	    {
	        if(a[j]>a[j-1])
	        {
	            for(int k=j-2;k>=0;k--)
	            {
	                if(a[k]>a[k+1])
	                {
	                r=k+1;
	                break;
	                }
	            }
	            break;
	        }
	    }
	    cout<<r<<endl;
	}
	return 0;
}
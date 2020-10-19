#include<iostream>

using namespace std;

int main()
{
   int n;
   cin>>n;
   int num=0;
   int a[n];
   int k;
   cin>>k;

   for(int i=0;i<n;i++){
      cin>>a[i];

      if(i==k-1){
         num=a[i];
      }
   }
   int count=0;
   for(int i=0;i<n;i++){
      if(a[i]>=num&&a[i]>0){
         count++;
      }
   }
   cout<<count;
}
#include<iostream>
#include<string>
#include<cstring>
using namespace std;

char convert(char a){
   if(a>='A' && a<='Z'){
      return a+32;
   }

   return a;
}
int main()
{
   char a[100];
   cin>>a;
   for(int i=0;i<strlen(a);i++){
      a[i]=convert(a[i]);
   }
   for(int i=0;i<strlen(a);i++){
      if(a[i]!='a'&&a[i]!='e'&&a[i]!='i'&&a[i]!='o'&&a[i]!='u'&&a[i]!='y'){
         cout<<"."<<a[i];
      }
   }
}
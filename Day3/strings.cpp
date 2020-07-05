#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a,b,conc;
    int len1,len2;
    char s1,s2,s3;

    cin>>a;
    cin>>b;
    len1=a.size();
    len2=b.size();
    //cout<<len1<<" "<<len2;
    conc=a+b;
    
    s1=a[0];
    s2=b[0];

    a[0]=s2;
    b[0]=s1;
    
    cout<<len1<<" "<<len2;
    cout<<"\n"<<conc;
    cout<<"\n"<<a<<" "<<b;
    return 0;
}
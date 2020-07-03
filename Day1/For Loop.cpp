#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int a,b;
    cin>>a;
    cin>>b;
    string c[]={"","one","two","three","four","five","six","seven","eight","nine"};
    for(int i=a;i<=b;i++)
    {
        if(i>9)
        {
            if(i%2==0){
                cout<<"even\n";
            }
            else {
                cout<<"odd\n";
            }
        }
        else if(i>=1&&i<=9){
            cout<<c[i]<<"\n";
        }
    }
    return 0;
}
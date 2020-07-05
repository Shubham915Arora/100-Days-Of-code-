#include <bits/stdc++.h>

using namespace std;



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    string c[]={"one","two","three","four","five","six","seven","eight","nine"};
    // Write Your Code Here
    if(n>9){
        cout<<"Greater than 9";
    }
    else{
        cout<<c[n-1];
    }

    return 0;
}

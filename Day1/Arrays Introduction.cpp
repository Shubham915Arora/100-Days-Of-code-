#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    int N,i=0;
    cin>>N;
    int *A = new int[N];
    while(i<N){
        cin>>A[i] ;
        i++;
    }
   
    while(i>0)
    {
        cout<<A[--i]<<" ";
        
    }
    //while(std::cin>>A[i++]);
   // while(std::cout<<A[--N]<<' ' && N);
    delete[] A;
    return 0;
}
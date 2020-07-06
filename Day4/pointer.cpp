#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    int sum=a+b;
    int dif=a-b;
    a=sum;
    if(dif<0) 
    b=dif*-1;
    else 
    b=dif;    
    printf("%d\n%d", a, b);

    return 0;
}
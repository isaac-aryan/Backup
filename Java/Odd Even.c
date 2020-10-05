#include <stdio.h>

int main(int argc, const char * argv[]) {
    int num;
    printf("Program to check odd or even");
    scanf("%d",&num);
    if (num%2==0) {
        printf("It is an even number");
        
    }
    else
        printf("It is an odd number");
    return 0;
}

#include<stdio.h>
int main(){
    long long int n = 67280421310721;
    for (long long int i = 2; i < n; i++){
        if (i % (100000000) == 0) {
            printf("%.5f%\n",  (100.0 * i / n));
        }
        if (n % i == 0) {
            printf("\n%d - is not prime", n);
            break;      
        }  
    }
    printf("the number seems to be prime");
}

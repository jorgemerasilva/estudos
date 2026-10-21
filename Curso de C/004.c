
#include <stdio.h>

void main() {
    //Casting de tipos
    int inteiro = 10;
    float real = (float) inteiro; //Casting de int para float
    printf("The float after casting is: %.2f\n", real);


    float real02 = 3.14;
    int inteiro02 = (int) real02; //Casting de float para int
    printf("The integer after casting is: %i\n", inteiro02);

    float real03 = 3.141592653589793;
    printf("The double is: %.15f\n", (double)real03);
} 
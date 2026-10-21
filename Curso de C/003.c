#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>

void main() {
    //Caracteres
    char letra;
    letra = 'A';
    printf("The character is: %c\n", letra);

    //Numeros inteiros
    int numero = 5;
    printf("The integer is: %i\n", numero);

    short int numero02;
    numero02 = 10;
    printf("The short integer is: %i\n", numero02);

    long int numero03;
    numero03 = 1000000678;
    printf("The long integer is: %li\n", numero03);

    unsigned int numero04;
    numero04 = 4294967295;
    printf("The unsigned integer is: %u\n", numero04);

    unsigned short int numero05;
    numero05 = 65535;
    printf("The unsigned short integer is: %hu\n", numero05);

    unsigned long int numero06;
    numero06 = 4294967295;
    printf("The unsigned long integer is: %lu\n", numero06);

    //Numeros reais
    float real;
    real = 3.14;
    printf("The float is: %.2f\n", real);

    double real02;
    real02 = 3.141592653589793;
    printf("The double is: %.15f\n", real02);

    long double real03 = 3.1415926535897932384626433L;
    printf("The long double is: %.15Lf\n", real03);

    //Constantes
    const int MAX = 100;
    const float PI = 3.14159;


    /*

    Use /* para comentar varias linhas de codigo
    
    */

} 
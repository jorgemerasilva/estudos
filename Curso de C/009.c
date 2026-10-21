
#include <stdio.h>
#include <string.h>

void main() {
   //Operador de condição ternário
    int x, y, maior;
    printf("Digite dois numeros inteiros: ");
    scanf("%d %d", &x, &y);
    maior = x > y ? x : y;
    printf("Maior: %d", maior);

}
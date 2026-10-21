
#include <stdio.h>
#include <string.h>

void main() {
   int a = 1;
   int b = 2;
   printf("%i < %i | resutado: %i\n", a, b, a < b);
   printf("%i > %i | resutado: %i\n", a, b, a > b);
   printf("%i <= %i | resutado: %i\n", a, b, a <= b);
   printf("%i >= %i | resutado: %i\n", a, b, a >= b);
   printf("%i == %i | resutado: %i\n", a, b, a == b);
   printf("%i != %i | resutado: %i\n", a, b, a != b);


   //Operadores Lógicos &&
   int idade = 18;
    char name[] = "Jorge";

    //Os dois tem que ser verdadeiro
    if (idade >= 18 && strcmp(name, "Jorge") == 0) {
        printf("É maior de idade e seu nome é %s\n", name);
    } else {
        printf("Inválido\n");
    }


    //Apenas um tem que ser verdadeiro ||
    if (idade >= 18 || strcmp(name, "Jorge") == 0) {
        printf("É maior de idade e seu nome é %s\n", name);
    } else {
        printf("Inválido\n");
    }


    //Nega !
    int ativo = 0;
    if (!ativo)
    {
        printf("Ativando...");
    } else {
        printf("Já esta ativo!");
    }

}
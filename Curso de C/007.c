
#include <stdio.h>

void main() {
   int a = 1, b = -2, c = 3;

   //Positivo
   printf("Positive of 1 is %i\n", +a);
   printf("Positive of (-2) 1 is %i\n", +b);
   
   printf("Negative of 1 is %i\n", -a);
   printf("Negative of (-2) 1 is %i\n", -b);

   printf("Adicao 1 + (-2) = %i\n",a+b);

   printf("subtracao 1 - (-2) = %i\n",a-b);

   printf("divisao de -2/1 = %i\n",a/b);

   printf("multiplicacao de 2*5 = %i\n",a*c);

   printf("Modulo de 3%%2 = %i\n",3%2);
   
   //Encremento
   int numero = 10;
   printf("Pre-encremento %d", ++numero);
   printf("Pos-encremento %d", numero++);

   //Decremento
   printf("Pre-decremento %d", --numero);
   printf("Pre-decremento %d", numero--);

   //Pode fazer com os outro operadores +-*/%
    int e;
    e += 5;

    int b;
    b -= 2;

}
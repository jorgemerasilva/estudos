
#include <stdio.h>
#include <string.h>

void main() {
   //Estrutura condicional
   int x = 4;
   if (x % 2 == 0)
   {
    printf("Numero PAR!\n");
   } else {
    printf("Numero IMPAR!\n");
   }

   //exemplo 2
   int numero = 10;
   if ( numero < 0)
   {
        printf("%i is negative!\n", x);
   } else if (x == 0) {
        printf("% is positive!\n", x);
    } else {
        printf("%i is positive!\n", x);
    }

    //exemplo 3
    int opcao;
    printf("Digite 1 ou 2: ");
    scanf("%d", &opcao);

    switch (opcao)
    {
    case 1:
        printf("\nDigitou 1!");
        break;
    case 2:
        printf("\nDigitou 2!");
        break;
    
    default:
        printf("\n11Opcao invalida!");
        break;
    }
    
   
}
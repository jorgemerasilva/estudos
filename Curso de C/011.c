
#include <stdio.h>
#include <string.h>
enum dia
{
    domingo,
    segunda,
    terca,
    quarta,
    quinta,
    sexta,
    sabado
};

void main() {
   enum dia d;
   printf("Digite um dia da semana (0 a 6): ");
   scanf("%i", &d);
   switch (d)
   {
    case domingo:
        printf("Domingo!");
        break;
        
    case segunda:
        printf("Segunda!");
        break;

    case terca:
        printf("Terca!");
        break;

    case quarta:
        printf("Quarta!");
        break;

    case quinta:
        printf("Quinta!");
        break;

    case sexta:
        printf("Sexta!");
        break;

    case sabado:
        printf("Sabado!");
        break;
    
    default:
    printf("Opcao invalida!");
        break;
   }
}
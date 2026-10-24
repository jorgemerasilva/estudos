
#include <stdio.h>

void main()
{
    int entrada, verifica = 1;
    do
    {
        printf("Digite um numero inteiro: \n");
        scanf("%d", &entrada);
        if (entrada % 2 == 0)
            printf("O nnumero e par\n");
        else
            printf("O numero e impar\n");

    } while(verifica != -1);

}
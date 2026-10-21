
#include <stdio.h>

void main()
{
    //While
    int entrada = 1;
    while (entrada != 0)
    {
        printf("Voce gostaria de sair do programa:\n"
        "0 - Finalizar programa\n"
        "1 - Continuar programando\n");

        scanf("%d", &entrada);

    }

    //Do While
    do
    {
        printf("Voce gostaria de sair do programa:\n"
        "0 - Finalizar programa\n"
        "1 - Continuar programando\n");

        scanf("%d", &entrada);
        
    } while (entrada != 0);
}
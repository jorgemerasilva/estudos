
#include <stdio.h>

void main() {
    int age;
    float height;
    float weight;
    float imc;

    printf("What is your age? ");
    scanf("%i",&age);

    printf("What is your height (in meters)? ");
    scanf("%f",&height);//Exemplo de entrada: 1.75

    printf("What is your weight (in kg)? ");
    scanf("%f",&weight);//Exemplo de entrada: 70.5

    imc = weight / (height * height);
    printf("Your BMI is: %.2f\n", imc);

    printf("\n\nyour age is: %i\n"\
           "your height is: %.2f\n"\
           "your weight is: %.2f\n"\
           "Your BMI is: %.2f"\
        ,age, height, weight, imc);
}
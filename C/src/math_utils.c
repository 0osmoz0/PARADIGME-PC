#include <stdio.h>
#include <stdlib.h>
#include "../include/math_utils.h"

// Calcul de la somme des nombres pairs de 2 à n
int sum_even_numbers(int n) {
    if (n < 2) return 0;
    
    int sum = 0;
    for (int i = 2; i <= n; i += 2) {
        sum += i;
    }
    return sum;
}

// Calcul de la factorielle
long long factorial(int n) {
    if (n < 0) return -1; // Erreur
    if (n <= 1) return 1;
    
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

// Vérification si un nombre est premier
int is_prime(int n) {
    if (n < 2) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return 0;
    
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return 0;
    }
    return 1;
}

// Calcul du PGCD (algorithme d'Euclide)
int gcd(int a, int b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Affichage d'un tableau
void print_array(int arr[], int size) {
    printf("[");
    for (int i = 0; i < size; i++) {
        printf("%d", arr[i]);
        if (i < size - 1) printf(", ");
    }
    printf("]\n");
}

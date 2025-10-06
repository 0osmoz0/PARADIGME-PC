#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/math_utils.h"

// Structure pour les opérations
typedef struct {
    char operation;
    int a, b;
    int result;
} Operation;

// Fonction pour effectuer une opération
int perform_operation(char op, int a, int b) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return (b != 0) ? a / b : 0;
        case '%': return (b != 0) ? a % b : 0;
        case '^': {
            int result = 1;
            for (int i = 0; i < b; i++) result *= a;
            return result;
        }
        default: return 0;
    }
}

// Fonction pour calculer la somme des carrés des nombres pairs
int sum_squares_even(int n) {
    int sum = 0;
    for (int i = 2; i <= n; i += 2) {
        sum += i * i;
    }
    return sum;
}

int main(void) {
    printf("=== Exercice 2: Calculateur Avancé ===\n\n");
    
    // Test des opérations de base
    printf("Test des opérations de base:\n");
    Operation operations[] = {
        {'+', 15, 25, 0},
        {'-', 50, 30, 0},
        {'*', 7, 8, 0},
        {'/', 100, 4, 0},
        {'%', 17, 5, 0},
        {'^', 2, 10, 0}
    };
    
    int num_ops = sizeof(operations) / sizeof(operations[0]);
    for (int i = 0; i < num_ops; i++) {
        operations[i].result = perform_operation(
            operations[i].operation, 
            operations[i].a, 
            operations[i].b
        );
        printf("%d %c %d = %d\n", 
               operations[i].a, 
               operations[i].operation, 
               operations[i].b, 
               operations[i].result);
    }
    
    // Test de la somme des carrés des nombres pairs
    printf("\nTest de la somme des carrés des nombres pairs:\n");
    for (int n = 0; n <= 10; n++) {
        int result = sum_squares_even(n);
        printf("sum_squares_even(%d) = %d\n", n, result);
    }
    
    // Test avec des tableaux
    printf("\nTest avec des tableaux:\n");
    int numbers[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    
    printf("Tableau original: ");
    print_array(numbers, size);
    
    // Calculer la somme des éléments pairs
    int sum_even = 0;
    int count_even = 0;
    for (int i = 0; i < size; i++) {
        if (numbers[i] % 2 == 0) {
            sum_even += numbers[i];
            count_even++;
        }
    }
    
    printf("Somme des éléments pairs: %d\n", sum_even);
    printf("Nombre d'éléments pairs: %d\n", count_even);
    
    // Test de performance simple
    printf("\nTest de performance (calculs répétés):\n");
    int iterations = 1000000;
    printf("Exécution de %d itérations de sum_even_numbers(100)...\n", iterations);
    
    int total = 0;
    for (int i = 0; i < iterations; i++) {
        total += sum_even_numbers(100);
    }
    
    printf("Résultat: %d (vérification: %d * %d = %d)\n", 
           total, sum_even_numbers(100), iterations, 
           sum_even_numbers(100) * iterations);
    
    printf("\n=== Exercice 2 terminé avec succès! ===\n");
    return 0;
}

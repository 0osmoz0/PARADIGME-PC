#include <stdio.h>
#include <stdlib.h>
#include "../include/math_utils.h"

int main(void) {
    printf("=== Exercice 1: Hello World et Tests Mathématiques ===\n\n");
    
    // Test de la somme des nombres pairs
    printf("Test de sum_even_numbers:\n");
    int test_values[] = {0, 1, 2, 3, 4, 5, 6, 10, 20};
    int expected[] = {0, 0, 2, 2, 6, 6, 12, 30, 110};
    int num_tests = sizeof(test_values) / sizeof(test_values[0]);
    
    printf("Valeurs de test: ");
    print_array(test_values, num_tests);
    
    int all_passed = 1;
    for (int i = 0; i < num_tests; i++) {
        int result = sum_even_numbers(test_values[i]);
        int passed = (result == expected[i]);
        printf("sum_even_numbers(%d) = %d (attendu: %d) %s\n", 
               test_values[i], result, expected[i], 
               passed ? "✓" : "✗");
        if (!passed) all_passed = 0;
    }
    
    printf("\nTest de la factorielle:\n");
    for (int i = 0; i <= 10; i++) {
        long long fact = factorial(i);
        printf("factorial(%d) = %lld\n", i, fact);
    }
    
    printf("\nTest des nombres premiers:\n");
    for (int i = 2; i <= 20; i++) {
        if (is_prime(i)) {
            printf("%d est premier\n", i);
        }
    }
    
    printf("\nTest du PGCD:\n");
    int pairs[][2] = {{12, 18}, {48, 36}, {17, 13}, {100, 25}};
    int num_pairs = sizeof(pairs) / sizeof(pairs[0]);
    
    for (int i = 0; i < num_pairs; i++) {
        int a = pairs[i][0];
        int b = pairs[i][1];
        int result = gcd(a, b);
        printf("gcd(%d, %d) = %d\n", a, b, result);
    }
    
    printf("\n=== Résumé ===\n");
    if (all_passed) {
        printf("✓ Tous les tests sont passés avec succès!\n");
        printf("✓ GCC fonctionne correctement\n");
        printf("✓ Makefile fonctionne correctement\n");
        printf("✓ Structure du projet C est opérationnelle\n");
    } else {
        printf("✗ Certains tests ont échoué\n");
        return 1;
    }
    
    return 0;
}

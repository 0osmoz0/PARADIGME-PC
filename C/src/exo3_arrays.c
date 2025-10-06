#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "../include/math_utils.h"

// Fonction pour générer un tableau aléatoire
void generate_random_array(int arr[], int size, int max_value) {
    srand((unsigned int)time(NULL));
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % max_value;
    }
}

// Fonction pour trier un tableau (tri à bulles)
void bubble_sort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Fonction pour rechercher un élément dans un tableau trié
int binary_search(int arr[], int size, int target) {
    int left = 0, right = size - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    
    return -1; // Non trouvé
}

// Fonction pour calculer les statistiques d'un tableau
void calculate_stats(int arr[], int size, int *min, int *max, double *avg) {
    if (size == 0) return;
    
    *min = *max = arr[0];
    long long sum = 0;
    
    for (int i = 0; i < size; i++) {
        if (arr[i] < *min) *min = arr[i];
        if (arr[i] > *max) *max = arr[i];
        sum += arr[i];
    }
    
    *avg = (double)sum / size;
}

int main(void) {
    printf("=== Exercice 3: Manipulation de Tableaux ===\n\n");
    
    const int SIZE = 20;
    int numbers[SIZE];
    
    // Génération d'un tableau aléatoire
    printf("Génération d'un tableau aléatoire de %d éléments:\n", SIZE);
    generate_random_array(numbers, SIZE, 100);
    print_array(numbers, SIZE);
    
    // Calcul des statistiques
    int min, max;
    double avg;
    calculate_stats(numbers, SIZE, &min, &max, &avg);
    
    printf("\nStatistiques du tableau:\n");
    printf("Minimum: %d\n", min);
    printf("Maximum: %d\n", max);
    printf("Moyenne: %.2f\n", avg);
    
    // Tri du tableau
    printf("\nTri du tableau (tri à bulles):\n");
    bubble_sort(numbers, SIZE);
    print_array(numbers, SIZE);
    
    // Recherche binaire
    printf("\nTest de recherche binaire:\n");
    int search_values[] = {numbers[0], numbers[SIZE/2], numbers[SIZE-1], 999};
    int num_searches = sizeof(search_values) / sizeof(search_values[0]);
    
    for (int i = 0; i < num_searches; i++) {
        int target = search_values[i];
        int index = binary_search(numbers, SIZE, target);
        if (index != -1) {
            printf("Valeur %d trouvée à l'index %d\n", target, index);
        } else {
            printf("Valeur %d non trouvée\n", target);
        }
    }
    
    // Test de performance
    printf("\nTest de performance:\n");
    const int PERF_SIZE = 1000;
    int perf_array[PERF_SIZE];
    
    printf("Génération d'un tableau de %d éléments...\n", PERF_SIZE);
    generate_random_array(perf_array, PERF_SIZE, 1000);
    
    printf("Tri du tableau de %d éléments...\n", PERF_SIZE);
    clock_t start = clock();
    bubble_sort(perf_array, PERF_SIZE);
    clock_t end = clock();
    
    double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("Temps de tri: %.6f secondes\n", time_taken);
    
    // Vérification que le tableau est trié
    int is_sorted = 1;
    for (int i = 0; i < PERF_SIZE - 1; i++) {
        if (perf_array[i] > perf_array[i + 1]) {
            is_sorted = 0;
            break;
        }
    }
    
    printf("Tableau correctement trié: %s\n", is_sorted ? "✓" : "✗");
    
    // Test avec des fonctions mathématiques
    printf("\nTest avec les fonctions mathématiques:\n");
    int test_array[] = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
    int test_size = sizeof(test_array) / sizeof(test_array[0]);
    
    printf("Tableau de test: ");
    print_array(test_array, test_size);
    
    // Calculer la somme des carrés des éléments pairs
    int sum_squares = 0;
    for (int i = 0; i < test_size; i++) {
        if (test_array[i] % 2 == 0) {
            sum_squares += test_array[i] * test_array[i];
        }
    }
    
    printf("Somme des carrés des éléments pairs: %d\n", sum_squares);
    
    // Vérifier quels éléments sont premiers
    printf("Éléments premiers dans le tableau: ");
    for (int i = 0; i < test_size; i++) {
        if (is_prime(test_array[i])) {
            printf("%d ", test_array[i]);
        }
    }
    printf("\n");
    
    printf("\n=== Exercice 3 terminé avec succès! ===\n");
    return 0;
}

// c/bench_fact.c - À compléter
#include <stdio.h>
#include <time.h>
#include <stdbool.h>
#include "fact.h"

double bench(unsigned int n, int iters) {
    // TODO-1: chronométrer iters appels à fact_ull(n) en ignorant la valeur
    clock_t start = clock();
    bool overflow;
    for (int i = 0; i < iters; i++) {
        fact_ull(n, &overflow);
    }
    clock_t end = clock();
    return ((double)(end - start)) / CLOCKS_PER_SEC;
}

int main(void) {
    // TODO-2: appeler bench pour n=12 et n=20, iters=100000; afficher les durées
    printf("=== Benchmarks Factorielle C ===\n\n");
    
    int iters = 100000;
    unsigned int test_values[] = {12, 20};
    int num_tests = sizeof(test_values) / sizeof(test_values[0]);
    
    for (int i = 0; i < num_tests; i++) {
        unsigned int n = test_values[i];
        double duration = bench(n, iters);
        printf("fact_ull(%u) - %.6fs pour %d appels\n", n, duration, iters);
        printf("  Moyenne: %.2f μs par appel\n", duration / iters * 1000000);
    }
    
    return 0;
}

// c/fact.c - À compléter
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <stdbool.h>

// Retourne true s'il y a overflow dans next = acc * k
static bool will_overflow_ull(unsigned long long acc, unsigned int k) {
    // TODO-1: Utiliser ULLONG_MAX pour vérifier si acc * k dépasse la capacité
    
    // Indice: comparer acc > ULLONG_MAX / k pour éviter l'overflow
    return acc > ULLONG_MAX / k;
}

unsigned long long fact_ull(unsigned int n, bool *overflow) {
    // TODO-2: initialiser acc = 1, *overflow = false
    unsigned long long acc = 1ULL;
    *overflow = false;
    if (n==0) return 1ULL;
    if(n==1) return 1ULL;
    // TODO-3: pour k de 2 à n : si overflow imminent -> *overflow=true; return acc
    for (unsigned int k = 2; k <= n; k++) {
        if (will_overflow_ull(acc, k)) {
            *overflow = true;
            return acc;
        }
        acc *= k;
    }


   // TODO-4: sinon acc *= k
    return acc;
}

int main(int argc, char **argv) {
    // TODO-5: parser argv, vérifier que l'argument est bien un entier >= 0
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <entier>=0\n", argv[0]);
        return 1;
    }
    char *endptr;
    long n = strtol(argv[1], &endptr, 10);
    if (*endptr != '\0' || n < 0) {
        fprintf(stderr, "Erreur: l'argument doit être un entier >= 0\n");
        return 1;
    }
    bool overflow;
    unsigned long long result = fact_ull((unsigned int)n, &overflow);
    if (overflow) {
        printf("Overflow: %ld! est trop grand pour être représenté en unsigned long long\n", n);
    } else {
        printf("%ld! = %llu\n", n, result);
    }
    // TODO-6: appeler fact_ull et afficher un message clair
    return 0; // À adapter   
}

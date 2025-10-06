#ifndef FACT_H
#define FACT_H

#include <stdbool.h>

// Fonction pour calculer la factorielle avec détection d'overflow
unsigned long long fact_ull(unsigned int n, bool *overflow);

#endif // FACT_H

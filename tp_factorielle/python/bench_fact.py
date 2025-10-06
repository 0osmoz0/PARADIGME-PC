# python/bench_fact.py - À compléter
from time import perf_counter
from fact import fact

def bench(fn, n, iters=100_000):
    """
    Retourne la durée (en secondes) pour iters appels de fn(n).
    Attention: mesures indicatives (bruit, cache, turbo CPU...).
    """
    # TODO: chronométrer une boucle d'appels
    start = perf_counter()
    for _ in range(iters):
        fn(n)
    end = perf_counter()
    return end - start

def main():
    # TODO: pour n in (12, 20), appeler bench et afficher un résumé
    print("=== Benchmarks Factorielle ===\n")
    
    for n in [12, 20]:
        duration = bench(fact, n, 100_000)
        print(f"fact({n}) - {duration:.6f}s pour 100,000 appels")
        print(f"  Moyenne: {duration/100_000*1_000_000:.2f} μs par appel")

if __name__ == "__main__":
    main()
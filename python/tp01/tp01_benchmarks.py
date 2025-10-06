# tp01_benchmarks.py
"""
TP01 - Benchmarks et Comparaisons de Performance
Comparaison des performances entre approches impérative et fonctionnelle
"""

import time
from functools import reduce
from operator import add
from tp01_imperatif import (
    sum_even_loop, sum_squares_even_loop, factorial_loop, 
    fibonacci_loop, is_prime_loop, bubble_sort_loop
)
from tp01_fonctionnel import (
    sum_even_functional, sum_squares_even_functional, factorial_functional,
    factorial_recursive, fibonacci_recursive, fibonacci_tail_recursive,
    is_prime_functional, quicksort_functional
)

def benchmark_function(func, *args, iterations: int = 1000) -> float:
    """Mesure le temps d'exécution d'une fonction."""
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        times.append(end - start)
    
    return min(times)  # Retourne le meilleur temps

def benchmark_comparison():
    """Compare les performances des différentes approches."""
    print("=== TP01 - Benchmarks de Performance ===\n")
    
    # Configuration des tests
    test_cases = {
        "sum_even": [(10,), (100,), (1000,)],
        "sum_squares_even": [(10,), (100,), (1000,)],
        "factorial": [(10,), (15,), (20,)],
        "fibonacci": [(10,), (20,), (30,)],
        "is_prime": [(97,), (997,), (9973,)],
        "sort": [([64, 34, 25, 12, 22, 11, 90],), 
                (list(range(100, 0, -1)),),
                (list(range(1000, 0, -1)),)]
    }
    
    # Fonctions à comparer
    functions = {
        "sum_even": [
            ("Loop", sum_even_loop),
            ("Functional", sum_even_functional)
        ],
        "sum_squares_even": [
            ("Loop", sum_squares_even_loop),
            ("Functional", sum_squares_even_functional)
        ],
        "factorial": [
            ("Loop", factorial_loop),
            ("Functional", factorial_functional),
            ("Recursive", factorial_recursive)
        ],
        "fibonacci": [
            ("Loop", fibonacci_loop),
            ("Recursive", fibonacci_recursive),
            ("Tail-Recursive", fibonacci_tail_recursive)
        ],
        "is_prime": [
            ("Loop", is_prime_loop),
            ("Functional", is_prime_functional)
        ],
        "sort": [
            ("Bubble Sort", bubble_sort_loop),
            ("Quick Sort", quicksort_functional)
        ]
    }
    
    # Exécution des benchmarks
    for test_name, test_args_list in test_cases.items():
        print(f"\n--- {test_name.upper()} ---")
        
        for args in test_args_list:
            print(f"\nArguments: {args}")
            
            for func_name, func in functions[test_name]:
                try:
                    # Ajuster le nombre d'itérations selon la complexité
                    iterations = 1000
                    if test_name == "fibonacci" and args[0] > 25:
                        iterations = 10
                    elif test_name == "sort" and len(args[0]) > 100:
                        iterations = 100
                    
                    time_taken = benchmark_function(func, *args, iterations=iterations)
                    time_ms = time_taken * 1000
                    
                    print(f"  {func_name:<15}: {time_ms:8.4f} ms")
                    
                except Exception as e:
                    print(f"  {func_name:<15}: ERROR - {e}")

def memory_usage_test():
    """Test d'utilisation mémoire pour les grandes structures."""
    print("\n=== Test d'Utilisation Mémoire ===\n")
    
    import sys
    
    # Test avec de grandes listes
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        print(f"Taille de liste: {size}")
        
        # Génération de données
        data = list(range(size, 0, -1))
        
        # Test bubble sort
        start_mem = sys.getsizeof(data)
        bubble_result = bubble_sort_loop(data)
        end_mem = sys.getsizeof(bubble_result)
        print(f"  Bubble Sort: {end_mem - start_mem} bytes supplémentaires")
        
        # Test quicksort
        start_mem = sys.getsizeof(data)
        quick_result = quicksort_functional(data)
        end_mem = sys.getsizeof(quick_result)
        print(f"  Quick Sort:  {end_mem - start_mem} bytes supplémentaires")

def scalability_analysis():
    """Analyse de la scalabilité des algorithmes."""
    print("\n=== Analyse de Scalabilité ===\n")
    
    # Test de scalabilité pour sum_even
    print("Scalabilité - Sum Even:")
    sizes = [100, 1000, 10000, 100000]
    
    for size in sizes:
        loop_time = benchmark_function(sum_even_loop, size, iterations=100)
        func_time = benchmark_function(sum_even_functional, size, iterations=100)
        
        print(f"  n={size:6d}: Loop={loop_time*1000:6.2f}ms, Func={func_time*1000:6.2f}ms")
    
    # Test de scalabilité pour fibonacci (récursif vs itératif)
    print("\nScalabilité - Fibonacci:")
    sizes = [10, 20, 30, 35]
    
    for size in sizes:
        try:
            loop_time = benchmark_function(fibonacci_loop, size, iterations=100)
            tail_time = benchmark_function(fibonacci_tail_recursive, size, iterations=100)
            
            print(f"  n={size:2d}: Loop={loop_time*1000:6.2f}ms, Tail-Rec={tail_time*1000:6.2f}ms")
        except:
            print(f"  n={size:2d}: Timeout ou erreur")

def correctness_verification():
    """Vérifie que toutes les implémentations donnent les mêmes résultats."""
    print("\n=== Vérification de Correctitude ===\n")
    
    test_cases = [
        ("sum_even", 20, [sum_even_loop, sum_even_functional]),
        ("sum_squares_even", 10, [sum_squares_even_loop, sum_squares_even_functional]),
        ("factorial", 10, [factorial_loop, factorial_functional, factorial_recursive]),
        ("fibonacci", 15, [fibonacci_loop, fibonacci_tail_recursive]),
        ("is_prime", 97, [is_prime_loop, is_prime_functional])
    ]
    
    all_correct = True
    
    for test_name, test_value, functions in test_cases:
        results = []
        for func in functions:
            try:
                result = func(test_value)
                results.append(result)
            except Exception as e:
                print(f"  {test_name}: Erreur dans {func.__name__} - {e}")
                all_correct = False
                continue
        
        if len(set(results)) == 1:
            print(f"  {test_name}: ✓ Tous les résultats identiques ({results[0]})")
        else:
            print(f"  {test_name}: ✗ Résultats différents {results}")
            all_correct = False
    
    if all_correct:
        print("\n✓ Toutes les implémentations sont correctes!")
    else:
        print("\n✗ Certaines implémentations ont des problèmes!")

def main():
    """Fonction principale pour exécuter tous les benchmarks."""
    print("Démarrage des benchmarks...\n")
    
    # Vérification de correctitude d'abord
    correctness_verification()
    
    # Benchmarks de performance
    benchmark_comparison()
    
    # Tests de mémoire
    memory_usage_test()
    
    # Analyse de scalabilité
    scalability_analysis()
    
    print("\n=== Benchmarks terminés ===")

if __name__ == "__main__":
    main()

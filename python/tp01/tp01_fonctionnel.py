# tp01_fonctionnel.py
"""
TP01 - Approche Fonctionnelle
Programmation fonctionnelle avec map, filter, reduce et récursion
"""

from functools import reduce
from operator import add, mul

def sum_even_functional(n: int) -> int:
    """Calcule la somme des nombres pairs avec une approche fonctionnelle."""
    return sum(range(2, n + 1, 2))

def sum_squares_even_functional(n: int) -> int:
    """Calcule la somme des carrés des nombres pairs avec map/filter/reduce."""
    return reduce(add, map(lambda x: x * x, filter(lambda x: x % 2 == 0, range(n + 1))), 0)

def factorial_functional(n: int) -> int:
    """Calcule la factorielle avec reduce."""
    if n < 0:
        return -1
    return reduce(mul, range(1, n + 1), 1)

def factorial_recursive(n: int) -> int:
    """Calcule la factorielle avec récursion."""
    if n < 0:
        return -1
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def fibonacci_recursive(n: int) -> int:
    """Calcule le n-ième nombre de Fibonacci avec récursion."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_tail_recursive(n: int) -> int:
    """Calcule le n-ième nombre de Fibonacci avec récursion terminale."""
    def go(k: int, a: int, b: int) -> int:
        if k == 0:
            return a
        return go(k - 1, b, a + b)
    return go(n, 0, 1)

def is_prime_functional(n: int) -> bool:
    """Vérifie si un nombre est premier avec une approche fonctionnelle."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    return not any(n % i == 0 for i in range(3, int(n ** 0.5) + 1, 2))

def quicksort_functional(arr: list[int]) -> list[int]:
    """Trie un tableau avec l'algorithme de tri rapide fonctionnel."""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort_functional(left) + middle + quicksort_functional(right)

def map_functional(func, iterable):
    """Implémentation fonctionnelle de map."""
    return [func(x) for x in iterable]

def filter_functional(predicate, iterable):
    """Implémentation fonctionnelle de filter."""
    return [x for x in iterable if predicate(x)]

def reduce_functional(func, iterable, initial=None):
    """Implémentation fonctionnelle de reduce."""
    if not iterable:
        return initial
    
    if initial is None:
        result = iterable[0]
        iterable = iterable[1:]
    else:
        result = initial
    
    for item in iterable:
        result = func(result, item)
    
    return result

def compose(*functions):
    """Compose plusieurs fonctions."""
    def composed(x):
        return reduce(lambda acc, f: f(acc), reversed(functions), x)
    return composed

def pipe(*functions):
    """Pipe plusieurs fonctions (compose dans l'ordre normal)."""
    def piped(x):
        return reduce(lambda acc, f: f(acc), functions, x)
    return piped

def main() -> None:
    """Fonction principale pour tester les fonctions fonctionnelles."""
    print("=== TP01 - Approche Fonctionnelle ===\n")
    
    # Test de sum_even_functional
    print("Test de sum_even_functional:")
    for n in [0, 1, 2, 3, 4, 5, 6, 10, 20]:
        result = sum_even_functional(n)
        print(f"sum_even_functional({n}) = {result}")
    
    print("\nTest de sum_squares_even_functional:")
    for n in [0, 1, 2, 3, 4, 5, 6, 10]:
        result = sum_squares_even_functional(n)
        print(f"sum_squares_even_functional({n}) = {result}")
    
    print("\nTest de factorial_functional vs factorial_recursive:")
    for n in range(0, 11):
        fact_func = factorial_functional(n)
        fact_rec = factorial_recursive(n)
        print(f"n={n}: functional={fact_func}, recursive={fact_rec}")
    
    print("\nTest de fibonacci (récursif vs tail-recursive):")
    for n in range(0, 11):
        fib_rec = fibonacci_recursive(n)
        fib_tail = fibonacci_tail_recursive(n)
        print(f"n={n}: recursive={fib_rec}, tail-recursive={fib_tail}")
    
    print("\nTest de is_prime_functional:")
    for n in range(2, 21):
        if is_prime_functional(n):
            print(f"{n} est premier")
    
    print("\nTest de quicksort_functional:")
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Tableau original: {test_array}")
    sorted_array = quicksort_functional(test_array)
    print(f"Tableau trié: {sorted_array}")
    
    print("\nTest des fonctions utilitaires:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Numbers: {numbers}")
    print(f"map(square): {map_functional(lambda x: x*x, numbers)}")
    print(f"filter(even): {filter_functional(lambda x: x%2==0, numbers)}")
    print(f"reduce(sum): {reduce_functional(add, numbers, 0)}")
    
    print("\nTest de composition:")
    square = lambda x: x * x
    double = lambda x: x * 2
    composed = compose(square, double)
    piped = pipe(double, square)
    print(f"compose(square, double)(5) = {composed(5)}")
    print(f"pipe(double, square)(5) = {piped(5)}")

if __name__ == "__main__":
    main()

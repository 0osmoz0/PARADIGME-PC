# exo8_benchmarks.py
from time import perf_counter
from functools import reduce
from operator import add

def sum_even_loop(n: int) -> int:
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

def sum_even_sumgen(n: int) -> int:
    return sum(i for i in range(2, n + 1, 2))

def sum_even_mfr(n: int) -> int:
    return reduce(add, filter(lambda x: x % 2 == 0, range(n + 1)), 0)

def bench(fn, n: int, repeats: int = 5) -> float:
    # TODO: renvoyer le meilleur temps
    times = []
    for _ in range(repeats):
        start = perf_counter()
        fn(n)
        end = perf_counter()
        times.append(end - start)
    return min(times)

if __name__ == '__main__':
    # TODO: imprimer un petit tableau de résultats
    functions = [
        ("Loop", sum_even_loop),
        ("Sum+Gen", sum_even_sumgen),
        ("MFR", sum_even_mfr)
    ]
    
    test_values = [100, 1000, 10000]
    
    print(f"{'Function':<12} {'n':<8} {'Time (ms)':<12} {'Result':<8}")
    print("-" * 45)
    
    for name, func in functions:
        for n in test_values:
            time_ms = bench(func, n) * 1000  # Convert to milliseconds
            result = func(n)
            print(f"{name:<12} {n:<8} {time_ms:<12.4f} {result:<8}")
        print()

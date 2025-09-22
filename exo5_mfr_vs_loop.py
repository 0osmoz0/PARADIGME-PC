# exo5_mfr_vs_loop.py
from functools import reduce
from operator import add

def sum_sq_even_mfr(values: list[int]) -> int:
    # TODO: filter pairs > 0, map square, reduce add (init 0)
    filtered = filter(lambda x: x%2 == 0 and x > 0, values)
    mapped = map(lambda x: x**2, filtered)
    return reduce(add, mapped, 0)

def sum_sq_even_loop(values: list[int]) -> int:
    # TODO: boucle + accumulation
    total = 0
    for v in values:
        if v % 2 == 0 and v > 0:
            total += v ** 2
    return total


if __name__ == '__main__':
    data = [1, -2, 2, 3, 4, 6]
    # TODO: imprimer et comparer
    result_mfr = sum_sq_even_mfr(data)
    result_loop = sum_sq_even_loop(data)
    print(f"Data: {data}")
    print(f"Sum of squares of even >0 (mfr): {result_mfr}")
    print(f"Sum of squares of even >0 (loop): {result_loop}")
    print(f"Results are equal: {result_mfr == result_loop}")
    ...

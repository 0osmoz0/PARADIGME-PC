# exo6_recursion.py
def sum_even_rec(n: int) -> int:
    # TODO: récursif simple
    if n < 2:
        return 0
    if n % 2 == 0:
        return n + sum_even_rec(n - 2)
    else:
        return sum_even_rec(n - 1)

def sum_even_tail(n: int) -> int:
    # TODO: go(k, acc) -> pseudo tail-recursion
    def go(k: int, acc: int) -> int:
        if k < 2:
            return acc
        if k % 2 == 0:
            return go(k - 2, acc + k)
        else:
            return go(k - 1, acc)
    return go(n, 0)

def sum_even_iter(n: int) -> int:
    return sum(x for x in range(2, n + 1, 2))

if __name__ == '__main__':
    # TODO: assertions d'égalité pour plusieurs n
    for n in (0, 1, 2, 3, 10, 100):
        result_rec = sum_even_rec(n)
        result_tail = sum_even_tail(n)
        result_iter = sum_even_iter(n)
        print(f"n={n}: rec={result_rec}, tail={result_tail}, iter={result_iter}, equal={result_rec == result_tail == result_iter}")
    ...

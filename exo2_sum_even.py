# exo2_sum_even.py
def sum_even_loop(n: int) -> int:
    # TODO: boucle + accumulation
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total
def sum_even_comp(n: int) -> int:
    # TODO: sum(...) avec range / générateur
    return sum(i for i in range (n + 1) if i % 2 == 0)

if __name__ == '__main__':
    # TODO: imprimer les deux résultats pour n in (0,1,2,3,10) et vérifier l'égalité
    for n in (0, 1, 2, 3, 10):
        result_loop = sum_even_loop(n)
        result_comp = sum_even_comp(n)
        print(f"n={n}: loop={result_loop}, comp={result_comp}, equal={result_loop == result_comp}")
    ...

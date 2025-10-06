# python/fact.py - À compléter
def fact(n: int) -> int:
    """
    Factorielle itérative. Lève ValueError si n < 0.
    Exigences:
      - n doit être un int (pas float/bool/str) -> TypeError
      - n doit être >= 0 -> ValueError
    """
    # TODO-1: Type-check strict (refuser bool)
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n doit être un int")
    if n < 0:
        raise ValueError("n doit être >= 0")
    # TODO-2: Domaine (n >= 0)
    if n == 0:
        return 1
    # TODO-3: res = 1
    res = 1
    # TODO-4: boucle k=2..n: res *= k
    for k in range (2, n+ 1):
        res *= k
    # TODO-5: return res
    return res

if __name__ == "__main__":
    # TODO-6: parser sys.argv, afficher l'usage si mauvais nb d'arguments
    import sys
    if len(sys.argv) != 2:
        print (f"Usage: {sys.argv[0]} <n>")
        sys.exit(1)
    # TODO-7: convertir en int, appeler fact, afficher "<n>! = <résultat>"
    try:
      n=int(sys.argv[1])
      resultat = fact(n)
      print(f"{n}! = {resultat}")
    except (TypeError, ValueError) as e:
      print(e)
      sys.exit(1)


    # TODO-8: gérer proprement TypeError/ValueError avec code de retour ≠ 0
    pass

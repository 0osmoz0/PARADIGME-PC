# exo9_refactor_io.py
def process_imp(items: list[int]) -> int:
    # NE PAS MODIFIER (exemple impur)
    total = 0
    for x in items:
        if x % 2 == 0:
            print(f"pair:{x}")       # I/O
            total += x * x           # mutation du total
    return total

def process_pure(items: list[int]) -> tuple[int, list[str]]:
    # TODO: pas d'I/O, renvoyer (total, logs)
    total = 0
    logs = []
    for x in items:
        if x % 2 == 0:
            logs.append(f"pair:{x}")
            total += x * x
    return total, logs

def run_with_logger(items: list[int]) -> int:
    # TODO: appeler process_pure, puis imprimer les logs
    total, logs = process_pure(items)
    for log in logs:
        print(log)
    return total

if __name__ == '__main__':
    # TODO: comparer la sortie de process_imp et run_with_logger sur la même liste
    test_items = [1, 2, 3, 4, 5, 6]
    
    print("=== Version impure (process_imp) ===")
    result_imp = process_imp(test_items)
    print(f"Résultat: {result_imp}")
    
    print("\n=== Version pure + orchestration (run_with_logger) ===")
    result_pure = run_with_logger(test_items)
    print(f"Résultat: {result_pure}")
    
    print(f"\n=== Comparaison ===")
    print(f"Résultats identiques: {result_imp == result_pure}")
    
    print(f"\n=== Test de la fonction pure isolée ===")
    total, logs = process_pure(test_items)
    print(f"Total: {total}")
    print(f"Logs: {logs}")
    print("(Aucun print dans process_pure - logs retournés dans une liste)")

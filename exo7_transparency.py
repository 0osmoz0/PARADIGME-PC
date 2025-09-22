# exo7_transparency.py
import time
STATE = {"count": 0}

def f_impure(x: int) -> int:
    # TODO: violer la TR (ex: dépendre du temps ou d'un compteur global)
    STATE["count"] += 1
    return x + STATE["count"] + int (time.time() % 10000)

def f_pure(x: int) -> int:
    # TODO: version TR
    return x * 2 + 10
    ...

if __name__ == '__main__':
    # TODO: démonstration simple (impressions/assertions)
    print("=== Test de transparence référentielle ===")
    
    # Test avec la fonction pure
    print("\nFonction PURE (f_pure):")
    for i in range(3):
        result = f_pure(5)
        print(f"f_pure(5) = {result} (toujours le même résultat)")
    
    # Test avec la fonction impure
    print("\nFonction IMPURE (f_impure):")
    STATE["count"] = 0  # Reset du compteur
    for i in range(3):
        result = f_impure(5)
        print(f"f_impure(5) = {result} (résultat différent à chaque appel)")
    
    # Démonstration que f_pure respecte la TR
    print(f"\nDémonstration TR:")
    print(f"f_pure(10) == f_pure(10): {f_pure(10) == f_pure(10)}")
    print(f"f_impure(10) == f_impure(10): {f_impure(10) == f_impure(10)}")

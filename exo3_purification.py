# exo3_purification.py
STATE = {"tick": 0}

def impure_tick(step: int = 1) -> int:
    # NE PAS MODIFIER
    STATE["tick"] += step
    return STATE["tick"]

def pure_tick(current: int, step: int = 1) -> int:
    # TODO: version pure (pas d'accès à STATE)
    return current + step

if __name__ == '__main__':
    # TODO: démontrer la différence de comportement (répétabilité)
    print("Impure ticks:")
    for _ in range(3):
        print(impure_tick(2))
    print("Pure ticks:")
    current = 0
    for _ in range(3):
        current = pure_tick(current, 2)
        print(current)

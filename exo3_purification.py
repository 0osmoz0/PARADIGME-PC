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
    print("Impure ticks:", impure_tick(), impure_tick())
    print("Pure tick", pure_tick(0), pure_tick(0))

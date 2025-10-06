# exo1_counter.py
from __future__ import annotations

def increment(counter: dict[str, int], step: int = 1) -> None:
    """Incrémente counter['value'] de step et log l'état avant/après."""
    print(f"Avant: counter = {counter}")
    counter['value'] += step
    print(f"Après: counter = {counter}")

def main() -> None:
    counter = {'value': 0}
    increment(counter, 2)
    increment(counter, 2)
    increment(counter, 2)
    print(f"État final: counter = {counter}")

if __name__ == '__main__':
    main()

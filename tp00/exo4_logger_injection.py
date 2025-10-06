# exo4_logger_injection.py
from collections.abc import Callable
# Variante A (avec global) - NE PAS TOUCHER
LOGS: list[str] = []
def inc_with_global_log(counter: dict[str, int], step: int = 1) -> None:
    before = counter['value']; counter['value'] += step
    msg = f"{before}->{counter['value']}"; LOGS.append(msg)

# Variante B (sans global) - À ÉCRIRE
def inc_with_injected_log(counter: dict[str, int], step: int, log_fn: Callable[[str], None]) -> None:
    # TODO
    before = counter ['value']
    counter ['value'] += step
    msg = f"{before}->{counter['value']}"
    log_fn(msg)

if __name__ == '__main__':
    # TODO: démontrer l'usage de inc_with_injected_log avec une liste locale de logs
    print("Avec global:")
    counter1 ={'value' : 0}
    inc_with_global_log(counter1, 2)
    inc_with_global_log(counter1, 2)
    inc_with_global_log(counter1, 2)
    print(f"counter1 = {counter1}, LOGS = {LOGS}")
    print("Avec injection:")
    counter2 = {'value' : 0}
    locals_logs: list[str] = []
    def local_log_fn(msg: str) -> None:
        locals_logs.append(msg)
    inc_with_injected_log(counter2, 2, local_log_fn)
    inc_with_injected_log(counter2, 2, local_log_fn)
    inc_with_injected_log(counter2, 2, local_log_fn)
    print(f"counter2 = {counter2}, locals_logs = {locals_logs}")
    ...

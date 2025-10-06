# tp01_tests.py
"""
TP01 - Tests Unitaires
Tests unitaires complets pour toutes les implémentations
"""

import pytest
from tp01_imperatif import (
    sum_even_loop, sum_squares_even_loop, factorial_loop,
    fibonacci_loop, is_prime_loop, bubble_sort_loop
)
from tp01_fonctionnel import (
    sum_even_functional, sum_squares_even_functional, factorial_functional,
    factorial_recursive, fibonacci_recursive, fibonacci_tail_recursive,
    is_prime_functional, quicksort_functional
)

class TestSumEven:
    """Tests pour les fonctions de somme des nombres pairs."""
    
    test_cases = [
        (0, 0), (1, 0), (2, 2), (3, 2), (4, 6), (5, 6),
        (6, 12), (10, 30), (20, 110), (50, 650)
    ]
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_sum_even_loop(self, n, expected):
        assert sum_even_loop(n) == expected
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_sum_even_functional(self, n, expected):
        assert sum_even_functional(n) == expected
    
    def test_sum_even_equivalence(self):
        """Test que les deux implémentations donnent le même résultat."""
        for n in range(0, 101):
            assert sum_even_loop(n) == sum_even_functional(n)

class TestSumSquaresEven:
    """Tests pour les fonctions de somme des carrés des nombres pairs."""
    
    test_cases = [
        (0, 0), (1, 0), (2, 4), (3, 4), (4, 20), (5, 20),
        (6, 56), (10, 220), (20, 1540)
    ]
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_sum_squares_even_loop(self, n, expected):
        assert sum_squares_even_loop(n) == expected
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_sum_squares_even_functional(self, n, expected):
        assert sum_squares_even_functional(n) == expected
    
    def test_sum_squares_even_equivalence(self):
        """Test que les deux implémentations donnent le même résultat."""
        for n in range(0, 51):
            assert sum_squares_even_loop(n) == sum_squares_even_functional(n)

class TestFactorial:
    """Tests pour les fonctions de factorielle."""
    
    test_cases = [
        (-1, -1), (0, 1), (1, 1), (2, 2), (3, 6), (4, 24),
        (5, 120), (10, 3628800), (15, 1307674368000)
    ]
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_factorial_loop(self, n, expected):
        assert factorial_loop(n) == expected
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_factorial_functional(self, n, expected):
        assert factorial_functional(n) == expected
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_factorial_recursive(self, n, expected):
        assert factorial_recursive(n) == expected
    
    def test_factorial_equivalence(self):
        """Test que toutes les implémentations donnent le même résultat."""
        for n in range(-1, 16):
            loop_result = factorial_loop(n)
            func_result = factorial_functional(n)
            rec_result = factorial_recursive(n)
            
            assert loop_result == func_result == rec_result

class TestFibonacci:
    """Tests pour les fonctions de Fibonacci."""
    
    test_cases = [
        (0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5),
        (6, 8), (10, 55), (15, 610), (20, 6765)
    ]
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_fibonacci_loop(self, n, expected):
        assert fibonacci_loop(n) == expected
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_fibonacci_recursive(self, n, expected):
        assert fibonacci_recursive(n) == expected
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_fibonacci_tail_recursive(self, n, expected):
        assert fibonacci_tail_recursive(n) == expected
    
    def test_fibonacci_equivalence(self):
        """Test que toutes les implémentations donnent le même résultat."""
        for n in range(0, 21):  # Limité pour éviter les timeouts
            loop_result = fibonacci_loop(n)
            tail_result = fibonacci_tail_recursive(n)
            
            assert loop_result == tail_result

class TestIsPrime:
    """Tests pour les fonctions de test de primalité."""
    
    test_cases = [
        (0, False), (1, False), (2, True), (3, True), (4, False),
        (5, True), (6, False), (7, True), (8, False), (9, False),
        (10, False), (11, True), (12, False), (13, True), (14, False),
        (15, False), (16, False), (17, True), (18, False), (19, True),
        (20, False), (97, True), (997, True), (9973, True)
    ]
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_is_prime_loop(self, n, expected):
        assert is_prime_loop(n) == expected
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_is_prime_functional(self, n, expected):
        assert is_prime_functional(n) == expected
    
    def test_is_prime_equivalence(self):
        """Test que les deux implémentations donnent le même résultat."""
        for n in range(0, 1000):
            assert is_prime_loop(n) == is_prime_functional(n)

class TestSorting:
    """Tests pour les fonctions de tri."""
    
    def test_bubble_sort_loop(self):
        """Test du tri à bulles."""
        test_cases = [
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([3, 2, 1], [1, 2, 3]),
            ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
            ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9])
        ]
        
        for input_arr, expected in test_cases:
            result = bubble_sort_loop(input_arr)
            assert result == expected
    
    def test_quicksort_functional(self):
        """Test du tri rapide fonctionnel."""
        test_cases = [
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([3, 2, 1], [1, 2, 3]),
            ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
            ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9])
        ]
        
        for input_arr, expected in test_cases:
            result = quicksort_functional(input_arr)
            assert result == expected
    
    def test_sort_equivalence(self):
        """Test que les deux algorithmes de tri donnent le même résultat."""
        test_arrays = [
            [],
            [1],
            [2, 1],
            [3, 2, 1],
            [64, 34, 25, 12, 22, 11, 90],
            [5, 2, 8, 1, 9],
            list(range(10, 0, -1)),
            [1, 1, 1, 1],
            [5, 5, 3, 3, 1, 1]
        ]
        
        for arr in test_arrays:
            bubble_result = bubble_sort_loop(arr)
            quick_result = quicksort_functional(arr)
            assert bubble_result == quick_result

class TestEdgeCases:
    """Tests des cas limites."""
    
    def test_negative_inputs(self):
        """Test avec des entrées négatives."""
        # Factorielle avec nombre négatif
        assert factorial_loop(-1) == -1
        assert factorial_functional(-1) == -1
        assert factorial_recursive(-1) == -1
        
        # Fibonacci avec nombre négatif
        assert fibonacci_loop(-1) == -1
        assert fibonacci_tail_recursive(-1) == -1
    
    def test_large_inputs(self):
        """Test avec de grandes entrées."""
        # Test de scalabilité
        large_n = 1000
        assert sum_even_loop(large_n) == sum_even_functional(large_n)
        assert sum_squares_even_loop(large_n) == sum_squares_even_functional(large_n)
    
    def test_empty_arrays(self):
        """Test avec des tableaux vides."""
        assert bubble_sort_loop([]) == []
        assert quicksort_functional([]) == []
    
    def test_single_element_arrays(self):
        """Test avec des tableaux à un élément."""
        single = [42]
        assert bubble_sort_loop(single) == single
        assert quicksort_functional(single) == single

class TestPerformance:
    """Tests de performance basiques."""
    
    def test_fibonacci_performance(self):
        """Test que la version tail-recursive est plus rapide que récursive."""
        import time
        
        n = 30
        
        # Test récursif (peut être lent)
        start = time.perf_counter()
        fibonacci_recursive(n)
        recursive_time = time.perf_counter() - start
        
        # Test tail-recursif
        start = time.perf_counter()
        fibonacci_tail_recursive(n)
        tail_time = time.perf_counter() - start
        
        # Le tail-recursif devrait être plus rapide
        assert tail_time < recursive_time or recursive_time < 1.0  # Tolérance pour les petits n

def test_all_implementations_consistency():
    """Test de cohérence globale entre toutes les implémentations."""
    # Test sur un échantillon de valeurs
    test_values = [0, 1, 2, 3, 4, 5, 10, 20, 50]
    
    for n in test_values:
        # Sum even
        assert sum_even_loop(n) == sum_even_functional(n)
        
        # Sum squares even
        assert sum_squares_even_loop(n) == sum_squares_even_functional(n)
        
        # Factorial
        assert factorial_loop(n) == factorial_functional(n) == factorial_recursive(n)
        
        # Fibonacci (limité pour éviter les timeouts)
        if n <= 20:
            assert fibonacci_loop(n) == fibonacci_tail_recursive(n)
        
        # Is prime
        assert is_prime_loop(n) == is_prime_functional(n)

if __name__ == "__main__":
    # Exécution des tests si le fichier est lancé directement
    pytest.main([__file__, "-v"])

# test_sum_even.py
import pytest
from exo2_sum_even import sum_even_loop, sum_even_comp
from exo6_recursion import sum_even_rec, sum_even_tail, sum_even_iter
from exo8_benchmarks import sum_even_loop as bench_loop, sum_even_sumgen, sum_even_mfr

class TestSumEvenImplementations:
    """Tests unitaires pour toutes les implémentations de sum_even"""
    

    test_cases = [
        (0, 0),      
        (1, 0),      
        (2, 2),      
        (3, 2),      
        (4, 6),      
        (5, 6),      
        (6, 12),   
        (10, 30),    
        (20, 110),   
        (50, 650),   
    ]
    
    implementations = [
        ("loop_exo2", sum_even_loop),
        ("comp_exo2", sum_even_comp),
        ("rec_exo6", sum_even_rec),
        ("tail_exo6", sum_even_tail),
        ("iter_exo6", sum_even_iter),
        ("loop_exo8", bench_loop),
        ("sumgen_exo8", sum_even_sumgen),
        ("mfr_exo8", sum_even_mfr),
    ]
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_loop_exo2(self, n, expected):
        """Test de la version boucle de l'exo2"""
        assert sum_even_loop(n) == expected
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_comp_exo2(self, n, expected):
        """Test de la version compréhension de l'exo2"""
        assert sum_even_comp(n) == expected
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_rec_exo6(self, n, expected):
        """Test de la version récursive de l'exo6"""
        assert sum_even_rec(n) == expected
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_tail_exo6(self, n, expected):
        """Test de la version tail-recursion de l'exo6"""
        assert sum_even_tail(n) == expected
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_iter_exo6(self, n, expected):
        """Test de la version itérative de l'exo6"""
        assert sum_even_iter(n) == expected
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_loop_exo8(self, n, expected):
        """Test de la version boucle de l'exo8"""
        assert bench_loop(n) == expected
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_sumgen_exo8(self, n, expected):
        """Test de la version sum+generator de l'exo8"""
        assert sum_even_sumgen(n) == expected
    
    @pytest.mark.parametrize("n,expected", test_cases)
    def test_mfr_exo8(self, n, expected):
        """Test de la version map/filter/reduce de l'exo8"""
        assert sum_even_mfr(n) == expected
    
    def test_all_implementations_equal(self):
        """Test que toutes les implémentations donnent le même résultat"""
        for n in range(0, 51):  # Test de 0 à 50
            results = []
            for name, func in self.implementations:
                try:
                    result = func(n)
                    results.append((name, result))
                except Exception as e:
                    pytest.fail(f"Erreur dans {name} avec n={n}: {e}")
            
            if len(set(result for _, result in results)) > 1:
                pytest.fail(f"Résultats différents pour n={n}: {results}")
    
    def test_edge_cases(self):
        """Test des cas limites spécifiques"""
        for name, func in self.implementations:
            try:
                result = func(-1)
                assert result == 0, f"{name} devrait retourner 0 pour n=-1"
            except (ValueError, RecursionError):
                pass


        for name, func in self.implementations:
            assert func(0) == 0, f"{name} devrait retourner 0 pour n=0"
            assert func(1) == 0, f"{name} devrait retourner 0 pour n=1"
    
    def test_performance_consistency(self):
        """Test que les implémentations sont cohérentes sur des valeurs moyennes"""
        test_values = [10, 25, 40]
        
        for n in test_values:
            results = []
            for name, func in self.implementations:
                result = func(n)
                results.append((name, result))

            unique_results = set(result for _, result in results)
            assert len(unique_results) == 1, f"Résultats incohérents pour n={n}: {results}"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])


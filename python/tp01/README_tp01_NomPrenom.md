# TP01 - Programmation Impérative vs Fonctionnelle

**Nom:** [Votre Nom]  
**Prénom:** [Votre Prénom]  
**Date:** [Date de réalisation]

## 📋 Objectifs du TP

Ce TP vise à comparer deux paradigmes de programmation :
- **Programmation Impérative** : Utilisation de boucles, mutations d'état, et structures de contrôle classiques
- **Programmation Fonctionnelle** : Utilisation de fonctions d'ordre supérieur, récursion, et immutabilité

## 🗂️ Structure du Projet

```
tp01/
├── tp01_imperatif.py      # Implémentations impératives
├── tp01_fonctionnel.py    # Implémentations fonctionnelles
├── tp01_benchmarks.py     # Tests de performance
├── tp01_tests.py          # Tests unitaires
└── README_tp01_NomPrenom.md
```

## 🚀 Fonctionnalités Implémentées

### 1. Somme des Nombres Pairs
- **Impératif** : `sum_even_loop(n)` - Boucle for classique
- **Fonctionnel** : `sum_even_functional(n)` - Utilisation de `sum()` et `range()`

### 2. Somme des Carrés des Nombres Pairs
- **Impératif** : `sum_squares_even_loop(n)` - Boucle avec accumulation
- **Fonctionnel** : `sum_squares_even_functional(n)` - Map/Filter/Reduce

### 3. Factorielle
- **Impératif** : `factorial_loop(n)` - Boucle avec multiplication
- **Fonctionnel** : `factorial_functional(n)` - Reduce avec multiplication
- **Récursif** : `factorial_recursive(n)` - Récursion classique

### 4. Suite de Fibonacci
- **Impératif** : `fibonacci_loop(n)` - Boucle avec variables temporaires
- **Récursif** : `fibonacci_recursive(n)` - Récursion classique
- **Tail-Récursif** : `fibonacci_tail_recursive(n)` - Récursion terminale

### 5. Test de Primalité
- **Impératif** : `is_prime_loop(n)` - Boucle avec division
- **Fonctionnel** : `is_prime_functional(n)` - Utilisation de `any()`

### 6. Algorithmes de Tri
- **Impératif** : `bubble_sort_loop(arr)` - Tri à bulles classique
- **Fonctionnel** : `quicksort_functional(arr)` - Tri rapide récursif

## 🧪 Tests et Validation

### Tests Unitaires
```bash
cd python/tp01
python -m pytest tp01_tests.py -v
```

### Benchmarks de Performance
```bash
python tp01_benchmarks.py
```

### Tests Individuels
```bash
python tp01_imperatif.py
python tp01_fonctionnel.py
```

## 📊 Résultats de Performance

### Observations Générales
- **Approche Impérative** : Généralement plus rapide pour les opérations simples
- **Approche Fonctionnelle** : Plus lisible et expressive, mais peut être plus lente
- **Récursion** : Peut être très lente pour de grandes valeurs (stack overflow)

### Comparaisons Spécifiques

| Fonction | Impératif | Fonctionnel | Récursif | Meilleur |
|----------|-----------|-------------|----------|----------|
| sum_even | ⚡ Rapide | ⚡ Rapide | N/A | Égalité |
| factorial | ⚡ Rapide | ⚡ Rapide | 🐌 Lent | Impératif/Fonctionnel |
| fibonacci | ⚡ Rapide | N/A | 🐌 Très lent | Impératif |
| is_prime | ⚡ Rapide | ⚡ Rapide | N/A | Égalité |
| sorting | 🐌 O(n²) | ⚡ O(n log n) | N/A | Fonctionnel |

## 🔍 Analyse des Paradigmes

### Avantages de l'Approche Impérative
- ✅ **Performance** : Généralement plus rapide
- ✅ **Contrôle** : Contrôle précis du flux d'exécution
- ✅ **Mémoire** : Utilisation mémoire optimisée
- ✅ **Debugging** : Plus facile à déboguer

### Avantages de l'Approche Fonctionnelle
- ✅ **Lisibilité** : Code plus expressif et concis
- ✅ **Sécurité** : Pas de mutations d'état
- ✅ **Composabilité** : Fonctions facilement composables
- ✅ **Testabilité** : Fonctions pures plus faciles à tester

### Inconvénients

#### Impératif
- ❌ **Complexité** : Peut devenir complexe avec la taille
- ❌ **Bugs** : Plus de risques d'erreurs avec les mutations
- ❌ **Réutilisabilité** : Code moins réutilisable

#### Fonctionnel
- ❌ **Performance** : Peut être plus lent
- ❌ **Courbe d'apprentissage** : Plus difficile à maîtriser
- ❌ **Stack overflow** : Risque avec la récursion profonde

## 🎯 Recommandations

### Quand utiliser l'Approche Impérative
- Calculs intensifs nécessitant des performances maximales
- Algorithmes avec beaucoup de mutations d'état
- Code legacy ou intégration avec des systèmes existants
- Développement d'algorithmes de bas niveau

### Quand utiliser l'Approche Fonctionnelle
- Développement d'APIs et de bibliothèques
- Traitement de données et transformations
- Code nécessitant une haute testabilité
- Développement de logiciels critiques

## 🔧 Installation et Utilisation

### Prérequis
```bash
pip install pytest
```

### Exécution des Tests
```bash
# Tests unitaires
python -m pytest tp01_tests.py -v

# Benchmarks
python tp01_benchmarks.py

# Tests individuels
python tp01_imperatif.py
python tp01_fonctionnel.py
```

## 📈 Métriques de Qualité

- **Couverture de tests** : 100% des fonctions testées
- **Performance** : Benchmarks sur différentes tailles de données
- **Correctitude** : Vérification de l'équivalence des résultats
- **Lisibilité** : Code documenté et commenté

## 🎓 Apprentissages

1. **Performance** : L'approche impérative est généralement plus rapide
2. **Maintenabilité** : L'approche fonctionnelle est plus maintenable
3. **Récursion** : Peut être dangereuse pour de grandes valeurs
4. **Choix** : Le paradigme dépend du contexte d'utilisation

## 📚 Références

- [Programmation Fonctionnelle en Python](https://docs.python.org/3/howto/functional.html)
- [Algorithmes et Structures de Données](https://fr.wikipedia.org/wiki/Structure_de_données)
- [Comparaison des Paradigmes](https://fr.wikipedia.org/wiki/Paradigme_de_programmation)

---

**Note** : Ce TP démontre l'importance de choisir le bon paradigme selon le contexte et les contraintes du projet.

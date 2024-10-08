# Fonctions et tableau

## 5. Génération de tableau à l'aide de fonctions Numpy

Une autre manière de créer ou générer un tableau Numpy est l'utilisation de fonctions comme dans les exemples ci-dessous :

```python

# Créer un tableau de 3 zéros.
np.zeros(3)

# Créer un tableau de dimension 2 lignes et 3 colonnes que de 1.
np.ones((2,3))

# Remplir un tableau d'une seule valeur, tableau de 2 lignes 3 colonnes
# avec la valeur 4.5
np.full((2,3), 4.5)

```

Vous pouvez également générer un tableau de valeur(s) "vide(s)", Numpy créera un tableau de valeur(s) aléatoire(s) de manière très optimisée :

```python
# Tableau 6 lignes et 2 colonnes
tmp = np.empty((6, 2) dtype='float32')

```

# Suppression et sélection

## Suppression de valeur dans une série méthode drop

Vous pouvez supprimer une valeur ou des valeurs dans une série à l'aide de la méthode drop.

```python
s = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])

# supprime une valeur
new_s = s.drop('c')

# supprime un ensemble de valeurs
new_s = s.drop(['a', 'c'])
```

## Sélection de valeurs dans une série

Pour la sélection vous pouvez accéder à une valeur à l'aide de son index numérique ou nommé :

```python
s = pd.Series( np.arange(4, 8), index=['a', 'b', 'c', 'd'] )

"""
a    4
b    5
c    6
d    7
"""

# affichera 4
s[0]

# affichera 4 également
s['a']
```

### "Slicing" sur les séries Pandas

Par rapport aux listes Python la syntaxe est légèrement différente avec les séries, voyez les exemples suivants :

```python
s['a':'c']

"""
a    4
b    5
c    6
"""
```

Ci-dessous, tous les index jusqu'à c, un index sur 2 :

```python
s[:'c':2]

"""
a    4
c    6
"""
```

Sur l'objet série il est également possible de sélectionner les valeurs selon un ordre souhaité :

```python
s[['b', 'a', 'b']]

"""
b    5
a    4
b    5
"""
```

Ceci marchera également avec les index numériques :

```python
s[[2, 1, 2]]

"""
b    5
a    4
b    5
"""
```

On peut également appliquer de l'indexation avancée sur une série ainsi dans l'exemple suivant on sélectionne toutes les valeurs supérieures à 4 et inférieures à 6 :

```python
s[ (s > 4) & (s < 6) ]
"""
b    5
"""
```

## Méthode sum

Par défaut la méthode *sum* de Pandas sur une série ignore les valeurs NaN.

```python

pd.Series([]).sum()
# 0

pd.Series([np.nan]).sum()
# 0
```

Il existe un paramètre **min_count** qui vaut soit 0 (valeur par défaut) soit 1.

Si vous mettez la valeur **min_count** à 1 alors vous aurez les résultats suivants :

```python
pd.Series([np.nan, np.nan, np.nan]).sum(min_count = 1)
# nan

pd.Series([np.nan, np.nan, np.nan, 9]).sum(min_count = 1)
# 9

pd.Series([]).sum(min_count = 1)
# nan
```

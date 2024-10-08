# Comptage et ordonner des valeurs

## Comptage de valeurs

Soit la Série A suivante :

```python

A = pd.Series(
    [12,9,10, 8, 10, 8 , np.nan],
    ['a', 'b', 'c', 'd', 'e', 'f', 'g']
)

A.unique()
# [ 12.,   9.,  10.,   8.,  nan]

A.value_counts()
"""
8.0     2
10.0    2
9.0     1
12.0    1
"""

```

**A.unique()** retourne un tableau Numpy des valeurs uniques.

**A.value_counts()** retourne une série avec pour chaque valeur le nombre d'occurence, trié par ordre d'occurence décroissant.

## Ordonner des valeurs d'une série

Vous pouvez ordonner la série sur les index ou les values :

```python
s = pd.Series( [10,3,8, 19, 2], index=['b', 'c', 'a', 'd', 'e'] )
s.sort_index()

"""
a     8
b    10
c     3
d    19
e     2
"""

s.sort_values()

"""
e     2
c     3
a     8
b    10
d    19
"""
```

Bien sûr vous pouvez préciser l'ordre avec le paramètre **ascending**, la valeur par défaut étant True par ordre croissant :

```python
s.sort_values(ascending=False)
"""
d    19
b    10
a     8
c     3
e     2
"""
```

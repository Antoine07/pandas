# Opérations

## 9. Opération avec les tableaux

Vous pouvez utiliser des opérateurs arithmétiques sur des tableaux, attention au sens de ces dernièrs, voyez les exemples qui suivent :

- L'addition additionne terme à terme les deux tableaux Numpy :

```python

numbers1 = np.array([1,2,3])
numbers2 = np.array([1,2,3])

numbers = numbers1 + numbers2

"""
array([2, 4, 6])
"""
```

- Diviser un array divise tous les termes :

```python

# Diviser un array
n = np.array([2, 4, 6])
n/2

"""
array([ 1.,  2.,  3.])
"""
```

Les autres opérateurs sont possibles sur les tableaux :

%, /, *, +

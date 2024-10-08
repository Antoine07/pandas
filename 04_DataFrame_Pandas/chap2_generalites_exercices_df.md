# Généralités

## Exercices manipulation des index & column

Remplacez à l'aide de la méthode replace de Pandas les données manquantes par np.nan de Numpy :

```python
df = pd.DataFrame(
    [
        [1, "2", None, 3],
        [4, None, "5", 6],
        [7, 8, 9, 10],
        ["None", "", None, "NAN"],
    ],
    index=['a', 'b', 'c', 'd'],
    columns = ['A', 'B', 'C', 'D']
)

```

## Exercice convertir un array Numpy en DataFrame

Redimensionnez la série suivantes en un DataFrame de dimension 3 lignes 5 colonnes, nommez les lignes a, b, c et les 5 colonnes avec d e f g h :

```python
A = pd.Series(np.random.randint(1, 10, 15))
```

## Exercice appliquer une fonction à un DataFrame

Soit le DataFrame C suivant :

```python

C = pd.DataFrame( np.random.randn(5, 5), columns=list("abcde"), index=list("fghij" ))

```

1. Mettez l'ensemble des valeurs en valeur absolue. Utilisez la fonction np.abs de Numpy.

2. Calculez l'amplitude des valeurs sur les lignes puis les colonnes. Vous pouvez utiliser la fonction apply sur le DataFrame.

## Exercice somme et remplacement

Soit le DataFrame suivant :

```python
C = pd.DataFrame( np.random.randn(5, 5), columns=list("abcde"), index=list("fghij"))
```

1. Faites la somme de toutes les valeurs négatives de C.

2. Remplacez dans la colonne b les valeurs négatives par la moyenne des valeurs positives de la colonne.

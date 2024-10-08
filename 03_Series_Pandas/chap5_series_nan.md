# Introduction aux données manquantes

## Les données manquantes NaN

Notons que le type des valeurs manquantes dans une série Pandas est NaN.

Python possède également un type None. En informatique et dans l'analyse des données cette valeur est très importante. Lorsque vous n'avez pas l'information ou la valeur de votre variable, la stratégie la plus cohérente est d'attribuer à celle-ci la valeur None ou np.nan pour Pandas.

Les deux fonctions suivantes permettent de tester les données manquantes dans un objet Series : **A.isnull()** retourne une série boolean. Notons également que vous avez la méthode pd.notnull(A) ou de manière équivalente A.notnull() qui retourne une série boolean True si la valeur existe et False si elle est NaN.

Avec Numpy si vous avez des données manquantes, il ne pourra pas, par exemple, calculer la moyenne des valeurs. Nous allons voir que ce n'est pas le cas avec une Séries.

```python
numbers = np.array([12,6,8,19, 10, np.nan , 14, np.nan])
print(numbers.mean()) # affiche nan

```

Avec une série dans Pandas la moyenne sera effectivement calculée, même avec des données manquantes, elles seront ignorées :

```python
numbers = pd.Series( [12,6,8,19, 10, np.nan , 14, np.nan] )
print(numbers.mean()) # affiche 11.5
```

Il est souvent utile de savoir combien il y a de donnée(s) manquante(s) dans une série. Dans ce cas vous utiliserez le code suivant :

```python
# ser une série quelconque
ser.isnull().sum()
```

## Exercice remplacer np.nan

Remplacez les valeurs np.nan par la moyenne de la série numbers.

# Création et index

## Exercice création d'objet "Séries" avec un dictionnaire Python

Voici une série Pandas pour représenter des villes et leur nombre d'habitants.

Sauriez-vous deviner ce que seront les index et les valeurs de l'objet Series dans l'exemple ci-dessous ?

```python
cities =  pd.Series({
    'Bordeaux' : 249712  ,
    'Paris' : 2190327 ,
    'Lille' : 232741
})
```

Quelle syntaxe devriez-vous utiliser pour accéder au nombre d'habitants à Paris ?

## Exercice construire des objets de type Séries

Créez maintenant un objet de type **Séries** ayant respectivement :

- Les valeurs:

```python
range(1, 12, 2)
```

- Et les index suivants :

```python
'abcdef'
```

## Exercice changez les index

Dans l'objet **Series** suivant :

```python
cities =  pd.Series({
    'Bordeaux' : 249712,
    'Paris' : 2190327,
    'Lille' : 232741
})
```

Mettez les codes respectifs des départements à la place des noms des villes dans la **Series** **cities**.

Bordeaux : 33, Paris : 75, Lille : 59

Puis sélectionnez uniquement les villes dont la population est supérieure à 2 000 000.

La population de chaque ville augmente de 10%, appliquez ce changement sur le dataset.

**Indications :** utilisez la méthode index de l'objet série pour les redéfinir.

## Exercice Series & index

Associez les index subjects ci-dessous à l'objet **Series** notes et calculez la moyenne générale de ces notes, donnez églament la médiane.

```python
notes = pd.Series([13.4, 20, 10, 15, 14, 16])

subjects = [
'Databases', 'Culture',
'Git', 'Stat desc',
'Stat inf', 'Python'
]
```

## Opération sur les Séries

On peut utiliser, comme dans Numpy, les opérations arithmétiques classiques sur les Séries. Il faudra cependant faire attention aux index. Les opérations s'alignent sur les index :

```python
a = pd.Series([1,2,3, 4], ['a', 'b', 'c', 'd' ])
b = pd.Series([10,20,30, 40], ['a', 'b', 'f', 'd' ])

a + b

"""
a    11.0
b    22.0
c     NaN
d    44.0
f     NaN

"""
```

## Re-indexer une Série

Vous pouvez ré-indexer une série à l'aide de la méthode **reindex**. Si les valeurs de la ré-indexation sont inférieurs ou supérieurs au nombre d'index, Pandas mettra NaN pour toutes correspondances non trouvées :

```python
a = pd.Series([1,2,3, 4], ['a', 'b', 'c', 'd' ])
print(a)
"""
a    1
b    2
c    3
d    4
"""
a = a.reindex(['d', 'b', 'a', 'c', 'f'])

# reindexé
"""
d    4.0
b    2.0
a    1.0
c    3.0
f    NaN
"""
```

Si les index sont moins nombreux alors des valeurs seront supprimées.

```python
a = a.reindex(['d', 'b'])
"""
d    4
b    2
"""
```

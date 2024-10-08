# Statistiques descriptives introduction

## Quartiles déciles

La méthode **qcut** permet de définir des tranches pour ranger les valeurs en quartiles, déciles, centiles... L'option labels de cette méthode permet de regrouper les données dans une tranche.

```python
ser = pd.Series(np.random.random(20))
pd.qcut(ser,
    q = [0, 0.25, .5, .75, 1],
    labels=['1 quartile', 'mediane', '3 quartile', '4 quartile']
)
```

On a pour la série ser les tranches :

- 0 à 0.25

- 0.25 à 0.5

- 0.5 à 0.75

- 0.75 à 1

Vous pouvez également utiliser une valeur numérique pour définir le nombre de tranches :

```python
pd.qcut(ser, 3, labels=['1', '2', '3'])
```

Sans l'argument labels qcut affichera l'ensemble des valeurs en précisant la tranche pour chacune d'entre elle.

## Information statistiques sur la Série

La méthode suivante retournera les informations de statistiques descriptives :

```python
A = pd.Series(np.random.random(20))
A.describe()

"""
count    20.000000
mean      0.375764
std       0.325878
min       0.022330
25%       0.111193
50%       0.194129
75%       0.642956
max       0.924646
"""
```

## Exercice notes et effectifs

```python
notes = pd.Series([1, 7, 8, 9, 10, 12, 15, 17, 18, 19 ,20])
effectifs = pd.Series([2,3, 2, 1, 5, 7, 2, 6, 2, 1, 1])
```

Les notes correspondent terme à terme aux effectifs.

1. Quel est le pourcentage d'étudiants de la promo Data01 ayant obtenu une note comprise entre 9 et 13 ?

2. Combien d'étudiants ont obtenus une note inférieur à 10 strictement.

3. Déterminez la moyenne de la promo.

4. Déterminez la note médiane.

5. Déterminez le premier et de dernier quartile.

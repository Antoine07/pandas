import pandas as pd
import numpy as np


## Exercice création de DataFrame

fruit1 = pd.DataFrame({
    'Rapsberry' : [30],
    'Cherries'  : [20]
})

fruit2 = pd.DataFrame({
    'fig' : [130, 309],
    'wine'  : [120, 290]
    }, index=['2020', '2019']
)

## Exercice construire des objets de type Séries

values = range(1, 12, 2)
index = 'abcdef'

A = pd.Series(list(values), list(index))

# Exercices changez les index

"""
Mettez les codes des départements à la place des noms des villes dans la Series : **cities_s**
Bordeaux : 33, Paris : 75, Lille : 59
"""

cities = {
    'Bordeaux' : 249712  ,
    'Paris' : 2190327 ,
    'Lille' : 232741
}

cities_s = pd.Series(cities)

#Bordeaux : 33, Paris : 75, Lille : 59
departements = [33, 75, 59]
cities_s.index = departements

# Augmentation de 10%
cities_s = cities_s * 1.1

## Exercice Series & index

notes = pd.Series([13.4, 20, 10, 15, 14, 16])

subjects = [
'Databases', 'Culture',
'Git', 'Stat desc',
'Stat inf', 'Python'
]

notes.index = subjects
print(notes.median())

## Exercice notes et effectifs

notes = pd.Series([1, 7, 8, 9, 10, 12, 15, 17, 18, 19 ,20])
effectifs = pd.Series([2, 3, 2, 1, 5, 7, 2, 6, 2, 1, 1])

# 1. Quel est le pourcentage d'étudiants de la promo Data01 ayant obtenu une note comprise entre 9 et 13 ?
perStudent = round( effectifs[ (notes > 8) & (notes < 14) ].sum() / effectifs.sum(), 2 ) * 100
print(perStudent)

# 2. Combien d'étudiants ont obtenus une note inférieur à 10 strictement.
nbStudent = effectifs[ notes < 10 ].sum()

# 3. Déterminez la moyenne de la promo.

average = (effectifs * notes).sum() / effectifs.sum()

# 4. Déterminez la note médiane.

Notes = np.repeat(notes, effectifs)

q1 = Notes.describe()['25%']
q3 = Notes.describe()['75%']

print(Notes.median(), q1, q3)

## Exercice apply

firstName = pd.Series([
    'adaline Reichel',
    'dr. Santa Prosacco DVM',
    'noemy Vandervort V',
    'lexi O Conner',
    'gracie Weber',
    'roscoe Johns',
    'emmett Lebsack',
    'keegan Thiel',
    'wellington Koelpin II',
    'ms. Karley Kiehn V',
])

## Exercice Séries A & B

#1. Soit les deux Séries A et B suivantes, récupérez les valeurs de la série A qui ne sont pas présentes dans la série B.
print(A.isin(B))
A[~A.isin(B)]

# 2.Donnez les valeurs de l'intersection de A et B.

print(A[A.isin(B)])

# 3. Quelles sont toutes les valeurs de A qui ne sont pas dans B et toutes les valeurs de B qui ne sont pas dans A.

data = pd.concat( [ B[~B.isin(A)], A[~A.isin(B)] ] , ignore_index=True)

print(data)


## Exercice Moyenne avec deux Séries
# 1. Moyenne des poids de chaque fruit
weights.groupby(fruits).mean()

# 2. Retournez tous les poids du fruit "banana". Donnez également le nombre de bananes.

# 2.1 Tous les poids du fruit bananes
print(weights[fruits == 'banana'])

# 2.2 Nombre de bananes
print( fruits[ fruits == 'banana' ].count() )

# 3. Ordonnez par somme des poids tous les fruits.
gw = weights.groupby(fruits).sum()
print(gw[ gw == gw.max()])
print(gw.sort_values(ascending=False))

## Exercice Remplacer et modifier

# Soit la chaîne de caractères suivantes :

characters ='abc def abe dae fab'

#1. Créez une Séries à partir de characters à l'aide de la méthode list.

#2.  Remplacez les espaces (caractères " ") par la valeur np.nan de Numpy.

#3. Trouvez la fréquence de la lettre la moins représentée dans la Séries, puis remplacez les valeurs NAN par cette lettre.


A = pd.Series( list( characters ) )

A[ A ==' '] = np.nan

letter = A.value_counts().index()
       
A.fillna(value = letter, inplace= True)

print("".join(A))

## Exercice serie temporelle

import pandas as pd
import numpy as np

ser = pd.Series(
    np.random.randint(100,200,30), 
    index = pd.date_range('2019-01-01', periods=30, freq='W')
)

print(ser.value_counts())

# dates pour les valeurs max et min
print( ser[ser == ser.max()] )
print( ser[ser == ser.min()] )

# somme des 5 dernières valeurs
print( ser[-5:].sum() )


# Méthode d'agrégation introduction

## Exercice méthode groupby

Soient les deux séries suivantes **fruits** et **weights**, calculez la moyenne des poids de chaques fruits. Utilisez la méthode **groupby**, elle permet de regrouper (agréger) des valeurs. Cette méthode ignorera les valeurs manquantes.

Retournez tous les poids du fruit "banana". Donnez également le nombre de bananes.

Quelle est le fruit qui a la somme de ses poids la plus élevée ?

Ordonnez par somme des poids les fruits.

```python
fruits = np.random.choice(['banana', 'apple', 'raspberry'], 15)
# Respectivement chaque poids correspond à chaque fruit
# linspace retourne un intervalle de valeurs entre 1 et 2
weights = np.linspace(1.0, 2.0, 15)
```

## Exercice ville et notes

On a récolté 100 notes d'internautes qu'ils ont attribué à trois villes différentes : Bordeaux, Lille et Paris. Ces valeurs sont données dans les deux tableau Numpy suivants :

```python
cities = np.random.choice(['Bordeaux', 'Lille', 'Paris'], 100)
notes = np.random.randint(0, 100, 100)
```

1. Créez les deux Séries cities_s et notes_s à partir de ces informations.

2. Donnez la moyenne de chaque ville.

3. Quelle(s) ville(s) a/ont eu la meilleur note des internautes ?

4. Y a t il une seule ville qui a eu plus de notes qu'une autre ?

La question suivante est un peu avancée, faites là si vous avez le temps et la motivation.

5. On définit maintenant des coefficients pour chacune des notes. Calculez la moyenne des notes par ville en  considérant ces coefficients.

```python
coeff = np.random.randint(1, 5, 100)
```

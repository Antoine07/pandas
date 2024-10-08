# Pandas

## Introduction générale

Pandas a été créé par Wes Mckinney (statisticien et développeur Python) dans le but d'analyser les données. Il est basé sur les structures de type array de Numpy que nous avons déjà présentées et comporte deux objets : les **DataFrame** et les **Series**.

- L'objet **Serie** est une liste de valeurs stockées dans une colonne identique à un array Numpy il est également semblable à un dictionnaire et possède en plus de l'indexation.

- Le **DataFrame** est un tableau à deux dimensions indexées. Un dataframe se comporte comme un dictionnaire dont les clefs sont les noms des colonnes et les valeurs sont des séries.

Avant de commencer vous pouvez configurer Pandas pour l'affichage des données dans votre notebook :

```python
import pandas as pd

pd.set_option('display.max_columns', 40)
pd.set_option('display.max_rows', 40)

```

## Documentation

Dans ce cours nous présentons des notions en abordant des exercices pratiques. Nous vous invitons à consulter la documentation pour compléter les définitions ou notions abordées :
[Documentation Pandas](https://pandas.pydata.org/pandas-docs/stable/)

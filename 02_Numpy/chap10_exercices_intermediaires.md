# Exercices supplémentaires

## Exercice minimum

Soit le tableau a suivant on cherche les valeurs minimales par ligne.

Nous aimerions à l'aide d'un script Python trouver tous les indices de tableau par ligne des minimaux et les enregistrer dans une liste de tuples comme dans l'exemple ci-dessous. Dans cette première version du programme si il existe plus d'un minimum par ligne vous enregistrerez la position du premier minimum trouvé.

```python

a = np.array([
    [13, 22, 28, 66, 40],
    [16, 59, 37, 33, 28],
    [34, 98, 54, 48, 96],
    [13, 84, 93, 79, 76],
    [63, 50, 12, 69, 12]
])

# Liste des minimaux et leur position sur chaque ligne
[(0, 13), (0, 16), (0, 34), (0, 13), (2, 12)]
```

Faites maintenant un deuxième programme permettant de récupérer toutes les positions de tous les minimaux par ligne :

```python
# Liste des minimaux et leur position sur chaque ligne
[(0, 13), (0, 16), (0, 34), (0, 13), (2, 12), (4, 12)]
```

\newpage

## Exercice éliminer les doublons

Dans le tableau suivant éliminer tous les doublons de lettres, voyez le tableau sanitize que nous aimerions avoir une fois votre script exécuté ci-dessous :

```python
a = np.array([
    ["aaabbfffhjik", "hhhkkkiooo", "hhjuuk"],
    ["rrrtttyyuuii", "rroooiiiuuu", "jjjhhhaa"],
    ["aaabbgghhh", "iiikkkooomml", "hhhiijjjuu"],
    ["hhhyyytttuu", "xxxnnnooii", "kkkjjjuuppp"],
    ["qqqfffgghhh", "qqqkkklll", "ooohhhjjj"],
])

sanitize = np.array([
       ['bfhajik', 'hiko', 'jhuk'],
       ['urity', 'urio', 'jha'],
       ['hgab', 'likmo', 'jhui'],
       ['hyut', 'xino', 'jupk'],
       ['fqhg', 'lqk', 'jho']
])
```

Indications : vous pouvez utiliser les set qui permettent d'obtenir un ensemble de valeurs uniques.

```python

print( set("aaabbfffhjik") )

```

\newpage

## Exercice formater/extraire des données

Développez un script permettant de nettoyer le dataset students pour obtenir le tableau sanitize :

```python

students = np.array([
    [  "Name: Luce du Coulon" , "phone: 201-20-30"],
    [  "Name: Auguste Dupont", "phone: 201-22-30"],
    [  "Name: Roger Le Voisi", "phone: 201-27-30"],
    [  "Name: Alexandre Lacri", "phone: 201-10-30"],
    [  "Name: Jacques Humber", "phone: 201-20-35"],
    [  "Name: Thérèse Guille", "phone: 201-20-38"],
    [  "Name: Gilles Gros-Bodin", "phone: 201-20-39"],
    [  "Name: Amélie Pires", "phone: 201-25-39"],
    [  "Name: Marcel Laporte", "phone: 201-20-39"],
    [  "Name: Geneviève Marchal", "phone: 301-20-39"]
])

santize = np.array([
       ['Luce du Coulon', '201-20-30']
       ['Auguste Dupont', '201-22-30']
       ['Roger Le Voisi', '201-27-30']
       ['Alexandre Lacri', '201-10-30']
       ['Jacques Humber', '201-20-35']
       ['Thérèse Guille', '201-20-38']
       ['Gilles Gros-Bodin', '201-20-39']
       ['Amélie Pires', '201-25-39']
       ['Marcel Laporte', '201-20-39']
       ['Geneviève Marchal', '301-20-39']
 ])

```

2. Comptez maintenant le nombre du numéro comportant le nombre 30.

Pour ce faire vous pouvez créer ce que l'on appelle un mask, c'est à dire parcourir le tableau et tester si le pattern "30" est présent dans la chaîne. Le mask devra avoir la même dimension que votre tableau. Une fois celui-ci en place vous pourrez alors l'appliquer de la manière suivante :

```python
sanitize[mask]
```

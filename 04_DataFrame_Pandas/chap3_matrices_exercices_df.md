# Matrice recherche & agrégation

## Exercice Matrice et recherche

Soit le tableau de valeurs numériques suivant. En utilisant la variable data ci-après construisez le DataFrame correspondant, respectez les noms des étiquettes (lignes et colonnes).

```text
 A   B   C   D   E   F   G   H   I   J
a  13  54  23  23  62  29  53  15  54  67
b  13  54  23  23  62  29  53  15  54  67
c  98  36  34  40  13  92  41  61  94  62
d  33  87  46  44  82  87  11  76  76  21
e  56  16  13  91  64  13  77  44  44  27
f  56  16  13  91  64  13  77  44  44  27
g  15  87  20  50  53  48  39  38  91  32
h  93  48  28  27  50  55  28  38  78  85
i  76  58  26  89  88  71  97  80  42  52
j  76  58  26  89  88  71  97  80  42  52
k  38  98  55  61  75  82  37  64  87  83
l  24  53  16  84  82  13  18  18  82  51
```

```python
 
data = [ 
    [13,  54,  23,  23,  62,  29,  53,  15,  54 , 67],
    [13,  54,  23,  23,  62,  29,  53,  15,  54,  67],
    [98,  36,  34,  40,  13,  92,  41,  61 , 94,  62],
    [33,  87,  46,  44,  82,  87,  11,  76,  76,  21],
    [56,  16 , 13,  91,  64,  13,  77,  44,  44,  27],
    [56,  16 , 13,  91,  64,  13,  77,  44,  44,  27],
    [15 , 87,  20,  50,  53,  48,  39,  38,  91,  32],
    [93,  48,  28,  27,  50 , 55 , 28 , 38  ,78 , 85],
    [76,  58 , 26  ,89 , 88  ,71 , 97 , 80,  42,  52],
    [76,  58 , 26  ,89 , 88  ,71 , 97 , 80,  42,  52],
    [38,  98,  55,  61,  75,  82 , 37,  64,  87,  83],
    [24,  53,  16,  84,  82,  13,  18,  18,  82,  51],
]
```

1. Recherchez toutes les lignes identiques dans le DataFrame et supprimez les. Vous pouvez utiliser la méthode **duplicated** sur le DataFrame.

2. Comptez les occurences de chaque valeur dans le DataFrame. Placez le résultat de ce comptage dans un dictionnaire voir ci-dessous la variable stat pour vérifier votre recherche.

*Indications : vous pouvez parcourir le DataFrame avec la méthode A.iterrows(), sur les étiquettes valeurs. Pensez à utiliser également les méthodes : count et sum.*

3. Faites la somme des nombres pairs de chaque ligne.


```python
stat ={13: 5, 54: 2, 23: 2, 62: 2, 29: 1, 53: 3, 15: 2, 
67: 1, 98: 2, 36: 1, 34: 1, 40: 1, 92: 1, 41: 1, 
61: 2, 94: 1, 33: 1, 87: 4, 46: 1, 44: 3, 82: 4, 
11: 1, 76: 3, 21: 1, 56: 1, 16: 2, 91: 2, 64: 2, 
77: 1, 27: 2, 20: 1, 50: 2, 48: 2, 39: 1, 38: 3, 
32: 1, 93: 1, 28: 2, 55: 2, 78: 1, 85: 1, 58: 1, 
26: 1, 89: 1, 88: 1, 71: 1, 97: 1, 80: 1, 42: 1, 
52: 1, 75: 1, 37: 1, 83: 1, 24: 1, 84: 1, 18: 2, 
51: 1}
```

## Exercice introduction aux notions d'agrégation

1. En utilisant **np.arange** et la méthode **.reshape** qui permet de changer les dimensions d'un array, générez la matrice A ci-dessous. Puis calculez les moyennes par lignes et colonnes de A en transposant la matrice. Voir un exemple de transposition ci-après.

Matrice A

```pyhton
  A  B  C  D  E  F  G  H  I
a 1  2  3  4  5  6  7  8  9 
b 2  4  6  8 10 12 14 16 18 
c 3  6  9 12 15 18 21 24 27 
d 4  8 12 16 20 24 28 32 36 
e 5 10 15 20 25 30 35 40 45 
f 6 12 18 24 30 36 42 48 54 
g 7 14 21 28 35 42 49 56 63 
h 8 16 24 32 40 48 56 64 72 
i 9 18 27 36 45 54 63 72 81
```

Transposition d'une matrice, elle change les dimensions des lignes/colonnes en colonnes/lignes

```python
C = pd.DataFrame( { "A" : [1, 2, 3, 4], "B" : [5, 6, 7, 8] } )

# Matrice B dimension 4 X 2
C
"""
   A  B
0  1  5
1  2  6
2  3  7
3  4  8
"""

C.T
"""
0  1  2  3
A  1  2  3  4
B  5  6  7  8
"""
```

Lorsque vous calculez la moyenne par ligne ou colonne d'un DataFrame, Pandas agrège les données pour effectuer ses calculs.

```python

# Agrégation de toutes les lignes
A.mean(axis = 0)

# Agrégation de toutes les colonnes
A.mean(axis = 1)

```

2. Ajoutez la matrice B à la seule colonne possible de la matrice A. Faites ensuite la somme en lignes, puis en colonnes en utilisant la notion de transposition.

```python
B = pd.DataFrame([11, 6, 4, 8, 0, 9, 7, 8, 13], index=list("abcdefghi"), columns=['A'])
```

3. Calculez les pourcentages des valeurs par ligne, puis par colonne en utilisant la technique de la transposée.

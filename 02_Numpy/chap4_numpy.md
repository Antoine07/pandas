# Les tableaux Numpy

## 4. Les tableaux dans Numpy

Les tableaux sont des structures de données propres à Numpy, très optimisés dans le stockage des données. Notons également qu'un tableau Numpy a un type unique. Les array Numpy sont également des objets mutables.

Si vous ne déterminez pas le type des éléments d'un tableau Numpy, celui-ci les convertira dans un type donné.

Vous pouvez lister tous les types possibles d'un tableau Numpy à l'aide de la commande suivante :

```python
import numpy as np

print(np.sctypes)
```

Retenez bien qu'un tableau aura un type défini et une longeur déterminée que l'on ne pourra pas changer.

Voici un tableau des types classiques dans Numpy :

- bool	Boolean (True or False)
- int8	Byte (-128 to 127)
- int16	Integer (-32768 to 32767)
- int32	Integer (-2 ** 31 to 2 ** 31 -1)
- int64	Integer (-2 ** 63 to 2 ** 63 -1)
- uint8	Unsigned integer (0 to 255)
- uint16	Unsigned integer (0 to 65535)
- uint32	Unsigned integer (0 to 2 ** 32 – 1)
- uint64	Unsigned integer (0 to 2 ** 64 – 1)
- float16 Half precision float: sign bit, 5 bits exponent, and 10 bits mantissa
- float32 Single precision float: sign bit, 8 bits exponent, and 23 bits mantissa
- float64 or float Double precision float: sign bit, 11 bits exponent, and 52 bits mantissa
- complex64 Complex number, represented by two 32-bit floats (real and imaginary components)
- complex128 or complex Complex number, represented by two 64-bit floats (real and imaginary components)

### 4.1 Type des tableaux Numpy

Nous vous conseillons de déterminer le type des données à la création d'un tableau.

Attention Numpy ne possède pas de notion Not a Number. Cela peut poser des problèmes dans la manipulation des données.

Cet exemple ne produira pas d'erreur et sera converti en float64

```python
np.array([1, 2, np.nan])
```

Cet exemple produira une erreur.

```python
np.array([1, 2, np.nan], dtype=int8)
```

Si vous ne déterminez pas le type des chaînes de caractères, Numpy fera une conversion silencieuse. Ci-dessous il prend du unicode et fixe la taille de la chaîne en prenant la taille de la plus longue chaîne du dataset :

```python
np.array(["Big data", "Python", "Pandas"])
# array(['Big data', 'Python', 'Pandas'], dtype='<U8')
```

On fixe la taille (préférable)

```python
np.array(["Big data", "Python", "Pandas"], dtype='<U8')
```

Dans ce dernier exemple toute chaîne de caractères qui dépasserait 8 caractères sera tronquée.

Un type peut également être "composite" comme dans l'exemple suivant :

```python

dt = np.dtype([
    ('name', np.dtype('U14')), ('grades', np.float64) 
])

dataset = np.array([
      ( "Luce du Coulon" , 12.5),
      ( "Auguste Dupont", 8.5),
      ( "Roger Le Voisi", 1.5)
], dtype=dt)

```

### 4.2 Création d'un array

Importez le module Numpy comme suit :

```python
import numpy as np

```

Vous pouvez alors définir un array avec une liste Python comme suit :

```python

# Array définition tableau d'une dimension
# dtype=int8 un entier sur 8 bits -128 à 127 = 256 entiers
numbers = np.array([1,2,3], dtype='int8')

# dtype du tableau
numbers.dtype

```

Remarques importantes

Une fois le type int8 entier sur 8 bits défini, si vous insérez dans votre tableau un entier qui dépasse cet encodage, Numpy le convertira. Voyez l'exemple ci-dessous :

```python

np.array([1, 2.8, 128], dtype='int8')
# conversion de 128 en -127
# [1, 2, -127]

```

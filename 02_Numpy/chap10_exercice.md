
# 3 Exercice fonction lambda

Soit le tableau suivant appliquez une augmentation de 10% sur chaque valeur paire du tableau suivant :

```python
prices = np.array([82, 92, 89, 65, 77, 66, 69, 65, 79, 51])
```

Indication : vous pouvez appliquer une fonction lambda avec un calcul simple sur le tableau lui-même. Pour filtrer les valeurs pairs utiliser la fonction np.where de Numpy

```python

rate = lambda x : x*1.1

rate(prices)
# Dans l'exemple suivant a est un tableau a > 2 est une condtion à vérifier sur toutes les valeurs du tableau et 1 et 0 les 
# valeurs à retourner en fonction de la condition si True 1 et False 0 :
np.where( a > 2, 1 , 0)

```

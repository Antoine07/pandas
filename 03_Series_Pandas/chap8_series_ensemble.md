# Les ensembles

## Exercice Séries A & B

1. Soit les deux Séries A et B suivantes, récupérez les valeurs de la série A qui ne sont pas présentes dans la série B.

2. Donnez les valeurs de l'intersection de A et B.

3. Quelles sont toutes les valeurs de A qui ne sont pas dans B et toutes les valeurs de B qui ne sont pas dans A.

*Pour ces questions, utilisez sur l'objet Séries de Pandas la méthode isin.*

```python
import pandas as pd

A = pd.Series([1,21,13,14,59])
B = pd.Series([14,21,3,4,5, 1])

```

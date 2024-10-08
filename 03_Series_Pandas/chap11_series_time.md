# Séries temporelles

## Exercice serie temporelle

*Sur une série temporelle vous avez la possiblité de définir des plages de dates, de définir des fréquences et d'utiliser des décalages sur les dates.*

Précisez le timezone de la série temporelle avec le paramètre **tz**.

```python
# D pour Day
s = pd.date_range('3/9/2019 9:30', periods=2, freq='D', tz='Europe/Paris')

"""
DatetimeIndex([
    '2019-03-09 09:30:00+01:00',
    '2019-03-10 09:30:00+01:00'],
    dtype='datetime64[ns, Europe/Paris]',
    freq='D'
)
"""
```

1. Créez une série de dates qui commence en 2019-01-01 (mardi 1 janvier 2019) et qui se termine 30 semaines plus tard, associez à chaque date un nombre aléatoire compris entre 100 et 200.

*Vous vous aiderez de la méthode **date_range**, cette méthode possède un argument **freq** pour préciser la fréquence entre les dates et **periods** ici 30.*

2. Trouvez maintenant les dates pour lesquelles la valeur aléatoire est la plus élevée. Même question pour la valeur min.

3. Faites la somme des valeurs pour les 5 dernières semaines.
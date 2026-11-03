---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"deletable": false, "editable": false, "grade_id": "cell-a8abc34598158c38", "tags": ["locked"]}

# Listes en compréhension

+++ {"deletable": false, "editable": false, "grade_id": "cell-cff6503f1009e98e", "tags": ["locked"]}

Les compréhensions sont un moyen confortable de construire des listes (ou autres
collections) en décrivant tous les éléments, avec une syntaxe proche de la notation
mathématiques pour l'ensemble des $f(x)$ pour $x$ dans $X$ tels que $c(x)$.

$$ \{ f(x) \mid  x\in X, c(x) \}$$

En Python la syntaxe est:

```
      [ <expr> for <name> in <iterable> ]
      [ <expr> for <name> in <iterable> if <condition> ]

```

Où :

- `expression` est l'opération ou la fonction à appliquer à chaque élément de l'itérable.
- `name` est une variable temporaire qui représente chaque élément de l'itérable.
- `iterable` est la liste ou l'objet itérable dont on souhaite traiter les éléments.
- `condition` est une condition optionnelle pour filtrer les éléments de l'itérable.

Supposons que nous ayons une liste de nombres et que nous voulions créer une nouvelle
liste contenant les carrés de ces nombres. Voici comment nous pourrions utiliser une
compréhension de liste pour accomplir cela :

```{code-cell} ipython3
nombres = [1, 2, 3, 4, 5]
carres = [x**2 for x in nombres]
print(carres)  # Résultat : [1, 4, 9, 16, 25]
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-d2eafc1f276bf8bb", "tags": ["locked"]}

Dans cet exemple, `x**2` est l'expression qui calcule le carré de chaque élément, et `x`
est la variable temporaire qui représente chaque élément de la liste nombres.

Il est possible d'ajouter une condition pour filtrer les éléments de la liste d'entrée.
Par exemple, si nous voulons obtenir les carrés des nombres pairs uniquement, nous
pouvons ajouter une condition if comme suit :

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-ebdb59dc076ef070
:tags: [locked]

nombres = [1, 2, 3, 4, 5]
carres_pairs = [x**2 for x in nombres if x % 2 == 0]
print(carres_pairs)  # Résultat : [4, 16]
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-7758e77483d04a39", "tags": ["locked"]}

Dans cet exemple, la condition `x % 2 == 0` vérifie si un nombre est pair.

[Source](https://www.docstring.fr/glossaire/comprehension-de-liste/)

+++ {"deletable": false, "editable": false, "grade_id": "cell-d7fe3ed2cd20d9c2", "tags": ["locked"]}

Voici un autre exemple : la liste des $i^2$ où $i$ est dans $\{1, 3, 7\}$:

```{code-cell} ipython3
[ i**2 for i in [1, 3, 7] ]
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-1d29f42da2c6e872", "tags": ["locked"]}

La même où $i$ parcoure l'intervale $[0, 10[$:

```{code-cell} ipython3
[ i**2 for i in range(0, 10) ]
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-c0d3f34585dc6103", "tags": ["locked"]}

La liste des $i^2$ dans l'intervale $[0,10[$ tels que $i$ n'est pas divisible par trois:

```{code-cell} ipython3
[ i**2 for i in range(0, 10) if i % 3 != 0]
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-b1cf338c017ead44", "tags": ["locked"]}

:::{admonition} Exercice
1. À partir de la liste `a` ci-dessous, construisez -- sans utiliser de compréhension -- une nouvelle liste `b` ne contenant
   que les valeurs de `a` supérieures à 5, en partant d'une liste vide et en ajoutant les
   éléments un à un avec la méthode `append`:
:::

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-7cec931945a7c64c
:tags: [locked]

a = [1, 4, 2, 7, 1, 9, 0, 3, 4, 6, 6, 6, 8, 3]
```

```{code-cell} ipython3
:deletable: false
:grade_id: cell-7ab7906710f62a88
:points: 0
:tags: [answer]

# Cellule cell-7ab7906710f62a88
b = []
# REMPLACEZ TOUTE CETTE LIGNE PAR VOTRE CODE
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-6238971b049d3283", "tags": ["locked"]}

:::{admonition} Exercice (suite)
2. Construisez à nouveau `b` en utilisant maintenant une compréhension.
:::

```{code-cell} ipython3
:deletable: false
:grade_id: cell-c5f9b4e21752301b
:points: 0
:tags: [answer]

# Cellule cell-c5f9b4e21752301b
# REMPLACEZ TOUTE CETTE LIGNE PAR VOTRE CODE
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-6199ad1605d76672", "tags": ["locked"]}

## Bilan

Les compréhensions offrent une notation concise, élégante et efficace pour construire une
liste en spécifiant les éléments qui la compose. Cette notation est proche de la notation
mathématique pour décrire un ensemble. Elle mets l'accent sur l'objet que l'on veut
construire plus que sur comment le construire.

C'est un principe très général: outre une meilleure compréhensibilité, exprimer ainsi
l'intention donne plus de latitude au système de calcul pour des optimisations. On
retrouve ce principe dans la programmation fonctionnelle et les idiomes de vectorisation
de Numpy, Pandas, etc.

```{code-cell} ipython3

```

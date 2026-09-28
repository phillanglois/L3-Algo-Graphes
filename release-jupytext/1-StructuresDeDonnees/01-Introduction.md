---
jupytext:
  notebook_metadata_filter: rise
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

+++ {"deletable": false, "editable": false, "grade_id": "cell-0fb472606b0a09e0", "tags": ["locked"]}

# Introduction aux graphes et leurs structures de données

## Graphes: quelques définitions

+++ {"deletable": false, "editable": false, "grade_id": "cell-12e390568ebd39f4", "tags": ["locked"]}

Qu'y a t'il de commun entre tous nos problèmes?

<!--TODO: figure!-->

+++ {"deletable": false, "editable": false, "grade_id": "cell-aad7f3cc33bd85bf", "tags": ["locked"]}

Dans chacun d'entre eux, la résolution se ramènera à étudier comment certains objets sont
reliés entre eux. Autrement dit, le problème va pouvoir être **modélisé à l'aide d'un
graphe**.

Informellement: un ***graphe*** est la donnée d'un ensemble de ***sommets*** reliés par
des ***arêtes***. Voilà un exemple avec cinq sommets. Les sommets 1 et 3 y sont reliés
entre eux. Mais pas 1 et 4.

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-12f9b9189e24d940
:tags: [locked]

import graph_networkx
G = graph_networkx.Graph(nodes=[1, 2, 3, 4, 5],
                         edges=[ (1,2), (1,3), (2,4), (3,4), (4,5) ])
G.show()
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-83378f7cd81fe8a0", "tags": ["locked"]}

La définition formelle la plus simple est la suivante:

:::{admonition} Définition
Un ***graphe*** est une paire $G:=(V,A)$ où $V$ est un ensemble et $A$ et un ensemble de
paires $\{v_1,v_2\}$ d'éléments de $V$.
:::

+++ {"deletable": false, "editable": false, "grade_id": "cell-cf0ad994eb573d6a", "tags": ["locked"]}

Dans notre exemple, $G=(V,A)$, où $V = \{1,2,3,4,5\}$ et
$A = \{\{1,2\}, \{1,3\}, \{2,4\}, \{3,4\}, \{4,5\} \}$.

+++ {"deletable": false, "editable": false, "grade_id": "cell-13c78db3c53e0610", "tags": ["locked"]}

:::{admonition} Remarque
Dans la définition donnée, une arête est un ensemble à deux éléments:

- le graphe n'est ***pas orienté***: si $s$ est relié à $t$ alors $t$ est relié à $s$;
- il n'y a pas de ***boucle***, c'est à dire une arête reliant un sommet à lui-même;
- ni d'***arête multiple***, c'est-à-dire plusieurs arêtes reliant les mêmes sommets;

On parle de ***graphe simple***.
:::

+++ {"deletable": false, "editable": false, "grade_id": "cell-bbf5fbc038ac698d", "tags": ["locked"]}

## Graphes: variantes

Le plus souvent, cette information de base est enrichie d'informations supplémentaires:
étiquettes sur les sommets, valuations sur les arêtes, orientation des arêtes, ...

On remplace la paire $\{v_1,v_2\}$ par un couple $(v_1,v_2)$ :

- On a en plus: orientation, boucle...

On ajoute un nombre à la paire $(v_1, v_2, c)$ :

- On a en plus: arête multiple, coût, capacité ...

+++ {"deletable": false, "editable": false, "grade_id": "cell-35c397cbf4956ace", "tags": ["locked"]}

## Quelques structures de données pour les graphes

Pour étudier un graphe à l'aide d'un ordinateur, il va falloir le représenter,
c'est-à-dire choisir une structure de données. Comme le champ d'application des graphes
et large, il y a beaucoup d'algorithmes différents, avec des besoins différents en terme
de performance des opérations élémentaires. Tel algorithme va demander d'avoir un accès
très performant aux voisins d'un sommet; tel autre parcourir les arêtes, etc. De ce fait,
il existe de nombreuses structures de données possibles que nous allons explorer
maintenant.

:::{attention}
On s'intéressera dans cette séance aux ***graphes orientés*** où chaque arête aura une
capacité `c` qui sera un nombre.
:::

+++ {"deletable": false, "editable": false, "grade_id": "cell-e65e3529dbc8309a", "tags": ["locked"]}

### Liste d'arêtes

+++ {"deletable": false, "editable": false, "grade_id": "cell-e65e3529dbc8309b", "tags": ["locked"]}

Ici, on représentera un graphe par une liste de triplets `(v1,v2,c)`, chacun d'entre eux
spécifiant qu'il y a une arête reliant $v_1$ à $v_2$ de capacité $c$.

+++ {"deletable": false, "editable": false, "grade_id": "cell-81506dd19fb33e98", "tags": ["locked"]}

Ci-dessous, nous donnons la structure de données `L0` d'un graphe $G_0$ avec trois
sommets, $0,1,2$, et deux arêtes; la première relie $0$ à $1$ avec une capacité de $10$
et la deuxième relie $0$ à $2$ avec une capacité de $4$.

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-832bab094684d111
:tags: [locked]

L0 = [ (0,1,10), (0,2,4) ]
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-53261b63230bc557", "tags": ["locked"]}

Voici la structure de donnée pour un autre graphe $G_1$:

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-9c8bb4f1b140e1aa
:tags: [locked]

L1 = [ (1,2,1), (1,3,1), (2,4,2), (3,4,0), (4,5,3) ]
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-9373d1fc68e76a53", "tags": ["locked"]}

:::{admonition} Exercice
Dessinez sur papier les graphes `G_0` et `G_1`, en mettant sur chaque arête sa capacité.
:::

+++

Pour chaque structure de données de ce cours, un type (laxiste) est fourni. Ici, ce sera:

```{code-cell} ipython3
graph_networkx.EdgeList
```

Ce type peut par exemple être utilisé pour typer statiquement du code ou pour faire des
vérifications dynamiques:

```{code-cell} ipython3
from typeguard import check_type
assert check_type(L1, graph_networkx.EdgeList)
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-b251ae3315043646", "tags": ["locked"]}

### Rappel: dictionnaires Python

+++ {"deletable": false, "editable": false, "grade_id": "cell-0964b25fb308a178", "tags": ["locked"]}

Un *dictionnaire* en Python est une structure de donnée permettant d'associer à une
valeur à une clé. Comme un dictionnnaire de français qui associe une définition à un mot,
ou un annuaire qui associe un numéro de téléphone à une personne. Voici un dictionnaire
qui associe la valeur `1` à la clé `"bla"`, la valeur `3` à la clé `"ble"` et la valeur
`"pi"` à la clé `3.13`:

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-3e5330e3a0b63562
:tags: [locked]

t = {"bla": 1, "ble": 3, 3.14: "pi"}
```

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-845e00c098b38b75
:tags: [locked]

t
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-6567db76a8c5039a", "tags": ["locked"]}

On peut accéder à une valeur à partir de sa clé avec l'opération suivante:

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-aa2d958877c70084
:tags: [locked]

t[3.14]
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-cc345264b87f4a1a", "tags": ["locked"]}

On notera la similitude avec l'accès aux éléments d'un tableau. On peut voir un tableau
de taille `l` comme un dictionnaire associant des valeurs à des clés entre `0` et `l-1`

+++ {"deletable": false, "editable": false, "grade_id": "cell-57228cfa27b007a1", "tags": ["locked"]}

### Dictionnaire des voisins

+++ {"deletable": false, "editable": false, "grade_id": "cell-2fea9135834106e0", "tags": ["locked"]}

Un sommet $v_2$ est un voisin sortant d'un sommet $v_1$ s'il y a une arête reliant $v_1$
à $v_2$.

On peut représenter un graphe à l'aide d'un ***dictionnaire des voisins*** qui à chaque
sommet associe la liste de ses voisins. Comme on veut représenter des capacités, la
valeur associée à la clé `v1` sera un liste de paires `(v2,c)` où $v_2$ sera le voisin et
`c` la capacité de l'arête reliant $v_1$ à $v_2$.

+++ {"deletable": false, "editable": false, "grade_id": "cell-20f20532263d1f73", "tags": ["locked"]}

Voici le dictionnaire des voisins pour $G_0$:

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-296573e3bba901c6
:tags: [locked]

DV0 = { 0: [(1,10), (2,4) ] }
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-d20bc2c5414d6b1a", "tags": ["locked"]}

:::{admonition} Exercice
Donnez le dictionnaire des voisins pour $G_1$, et stockez le dans la variable `DV1`:
:::

```{code-cell} ipython3
:deletable: false
:grade_id: cell-d662314d2272933e
:tags: [answer]

# Cellule cell-d662314d2272933e
# REMPLACEZ TOUTE CETTE LIGNE PAR VOTRE CODE
```

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-693333c71f3b0afb
:points: 1
:tags: [test]
:test: true

assert check_type(DV1, graph_networkx.NeighborDict)
assert sorted(L1) == sorted( (i,j, w) for i, l in DV1.items() for [j,w] in l )
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-b6d9d6f663f27355", "tags": ["locked"]}

:::{note}
Si les sommets du graphe sont étiquetés par $0,1,\ldots$, on peut utiliser une liste au
lieu d'un dictionnaire :
:::

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-e8e4a3fea4afa0c3
:tags: [locked]

# Avec un tableau (graphe etiquete par 0,1,...)
DV0 = [ [(1,10), (2,4)] ]
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-56783b8586212b07", "tags": ["locked"]}

### Dictionnaire d'arêtes

+++ {"deletable": false, "editable": false, "grade_id": "cell-853b0c46657a7984", "tags": ["locked"]}

Utilisons maintenant un ***dictionnaire d'arêtes*** pour représenter `G_1` : il associera
à chaque paire `(u1,v1)` reliés par une arête la capacité de cette arrête.

+++ {"deletable": false, "editable": false, "grade_id": "cell-853b0c46657a7983", "tags": ["locked"]}

Voici le dictionnaire pour $G_0$:

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-8b9c4f073bacba06
:tags: [locked]

DA0 = { (0,1): 10,
        (0,2): 4
      }
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-6bc88084fce0f9fa", "tags": ["locked"]}

:::{admonition} Exercice
Donnez le dictionnaire d'arêtes pour $G_1$.
:::

```{code-cell} ipython3
:deletable: false
:grade_id: cell-98fa5972274a0bce
:tags: [answer]

# Cellule cell-98fa5972274a0bce
# REMPLACEZ TOUTE CETTE LIGNE PAR VOTRE CODE
```

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-f7f112267dc6e5d5
:points: 1
:tags: [test]
:test: true

assert check_type(DA1, graph_networkx.EdgeDict)
assert sorted(L1) == sorted((i, j, c) for (i, j), c in DA1.items())
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-4ae02a19ea56aaa6", "tags": ["locked"]}

## Matrice d'adjacence

La ***matrice d'adjacence*** d'un graphe est un tableau (ou matrice) à deux dimensions
`M` tel que `M[v1,v2]` est la capacité `c` de l'arête reliant $v_1$ à $v_2$ ou $0$ s'il
n'y a pas d'arête.

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-9ab824cd1bb2aa61
:tags: [locked]

M0 = [ [0, 10, 4],
       [0,  0, 0],
       [0,  0, 0]]
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-33cf5a83c5bb4813", "tags": ["locked"]}

::::{admonition} Exercice
Donnez la matrice d'adjacence pour $G_1$.

:::{admonition} Indication
:class: tip dropdown

- Vous rajouterez un sommet $0$ (pourquoi?).
- Rappel: Le graphe est orienté.
:::
::::

```{code-cell} ipython3
:deletable: false
:grade_id: cell-9caa44fcb3382c31
:tags: [answer]

# Cellule cell-9caa44fcb3382c31
# REMPLACEZ TOUTE CETTE LIGNE PAR VOTRE CODE
```

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-6a73ce89b2eba610
:points: 1
:tags: [test]
:test: true

assert check_type(M1, graph_networkx.AdjacencyMatrix)
assert len(M1) == 6
assert all(len(M1[i]) == 6 for i in range(6))
assert sum( M1[i][j] for i in range(6) for j in range(6) ) == 7
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-3bd1311aa4b5829e", "tags": ["locked"]}

# Conclusion

Maintenant que vous avez manipulé des structures de données de graphes sur des exemples,
vous pouvez passer à la feuille suivante.

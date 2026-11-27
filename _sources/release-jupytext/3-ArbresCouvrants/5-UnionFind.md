---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"deletable": false, "editable": false}

# Stucture de données Union-Find

+++ {"deletable": false, "editable": false}

Dans l'algorithme de Kruskal, on a besoin de savoir en permanence si
les deux extrémités de l'arête considérée sont dans la même composante
connexe. Il serait très inefficace de refaire à chaque fois un
parcours. On a donc besoin d'une structure de données qui permet de
maintenir les composantes connexes du graphe partiel au cours de
l'algorithme.

+++ {"deletable": false, "editable": false}

La structure de données
[***Union-Find***](https://fr.wikipedia.org/wiki/Union-find)
représente une partition d'un ensemble fini. On rappelle qu'une
***partition d'un ensemble*** $E$ est un ensemble de parties
non vides de $E$ -- appelées ***classes*** -- qui sont deux à
deux disjointes et dont l'union est $E$. 

Dans notre application chaque composante connexe du graphe contribue
une classe de la partition, formée par l'ensemble de ses sommets.

+++ {"deletable": false, "editable": false}

L'idée d'Union-Find est de choisir, dans chaque classe, un
représentant dit «canonique». On va ensuite implémenter les deux
méthodes suivantes:
- `find(v)` : quel est le représentant de la classe de $v$.
- `union(u, v)` : mettre à jour la structure de données pour réunir
  les classes des représentants canoniques $u$ et $v$.

+++ {"deletable": false, "editable": false}

Pour cela, on va stocker une forêt orientée où chaque arbre couvre une
classe et a pour racine son représentant canonique.

Find se contente de remonter les liens vers les nœuds pères jusqu'à
atteindre la racine. Union réunit deux arbres en attachant la racine
de l'un comme fils de la racine de l'autre.

Vous pouvez trouver des détail sur
[Union-Find](https://fr.wikipedia.org/wiki/Union-find). Il existe
aussi une
[applet](http://www.irisa.fr/prive/fschwarz/mit1_algo2_2013/union_find/)
de simulation.

+++ {"deletable": false, "editable": false}

:::{admonition} Exercice

1.  Définissez une classe `UnionFind` implémentant les trois méthodes
    suivantes:
    - `UnionFind(S)` : constructeur (`__init__` en Python) qui
      initialize l'ensemble avec toutes les classes singletons
    - `UF.find(i)` : détermine l'élément canonique de la classe de `i`
    - `UF.union(i, j)` : réuni les classes associées à `i` et `j`

2.  Testez votre classe `UnionFind`.

3.  Implantez les deux optimisations suivantes :
    -   compression des chemins dans le cas d'un find : on reparcourt
        le chemin en associant directement le noeud canonique aux
        éĺéments du chemin. On écrira une version **itérative**;
    -   heuristique du rang pour diminuer la hauteur de l'arbre en cas
        d'union.

:::

La structure de données Union-Find donne un autre algorithme pour
calculer les composantes connexes :

- on part de la partition triviale (tous les sommets sont seuls dans
  leur classes)
- on appelle `union(i,j)` pour toutes les arêtes $i - j$.

À la fin, on obtient la partition des sommets en composantes connexes.

+++ {"deletable": false, "editable": false}

:::{admonition} Exercice

1.  Définissez une méthode `connected_componentsUF()`

2.  Vérifiez sur tous les graphes d'exemple qu'elle renvoie le même
    résultat que `connected_components()`.

3.  En utilisant `UnionFind`, implantez l'algorithme de Kruskal pour
    calculer l'arbre couvrant de poids minimum d'un graphe.

4.  Testez votre fonction sur tous les graphes d'exemple.

:::

+++ {"deletable": false, "editable": false}

## Application : Construction d'un labyrinthe

:::{admonition} Exercice

En partant du graphe grille $m*n$, construire un labyrinthe parfait à
l'aide d'un arbre couvrant. On pourra faire un affichage ASCII comme
ci-dessous.

:::

    +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
    |   |   |           |   |       |                   |       |   |               |
    +   +   +---+   +   +   +   +   +---+   +---+   +---+---+   +   +   +   +---+   +
    |       |   |   |   |       |   |       |               |       |   |   |   |   |
    +   +---+   +   +---+   +---+   +---+---+---+   +---+   +   +   +---+   +   +   +
    |   |           |           |   |       |       |   |   |   |           |       |
    +   +   +---+   +   +---+   +---+   +---+---+   +   +---+---+---+   +---+   +---+
    |           |   |       |   |                   |   |   |   |   |   |           |
    +   +   +---+   +---+   +---+   +   +---+---+---+   +   +   +   +---+   +---+   +
    |   |       |           |       |           |               |   |   |   |   |   |
    +---+---+---+---+---+   +---+   +---+---+---+   +---+---+   +   +   +   +   +   +
    |                           |                           |   |               |   |
    +---+   +---+---+   +   +---+---+   +---+   +---+---+---+   +   +---+---+---+---+
    |       |       |   |   |   |           |           |       |           |       |
    +---+---+   +---+   +   +   +   +---+---+   +---+---+---+   +   +---+   +---+   +
    |           |       |   |   |   |           |                       |       |   |
    +   +---+   +---+   +---+   +---+---+---+---+---+   +---+---+   +---+---+   +   +
    |   |   |       |   |   |   |   |   |               |   |       |   |           |
    +   +   +   +---+   +   +   +   +   +---+---+   +---+   +---+---+   +   +---+   +
    |   |               |           |       |   |                       |       |   |
    +   +---+---+   +   +---+   +---+   +---+   +   +---+---+   +---+---+---+   +---+
    |   |           |   |           |                   |           |       |   |   |
    +---+---+   +---+   +---+   +---+---+---+---+---+---+   +---+   +   +---+---+   +
    |       |   |                   |   |   |   |           |               |   |   |
    +---+   +   +---+   +   +   +---+   +   +   +   +---+   +---+   +   +---+   +   +
    |           |       |   |       |               |   |   |   |   |               |
    +---+   +   +   +---+   +   +   +   +---+---+---+   +   +   +---+---+---+---+---+
    |   |   |   |   |       |   |               |   |   |       |   |       |       |
    +   +   +---+   +---+   +---+   +   +---+---+   +   +   +   +   +---+   +   +---+
    |           |       |   |       |       |               |       |   |   |   |   |
    +---+   +---+---+---+---+---+   +---+   +   +   +---+   +---+   +   +   +   +   +
    |       |   |           |           |   |   |       |       |       |           |
    +   +---+   +---+   +---+---+---+---+---+---+   +---+---+   +---+   +   +---+---+
    |   |       |               |                   |           |   |       |   |   |
    +---+---+   +   +---+   +   +   +---+   +   +---+   +---+   +   +---+   +   +   +
    |           |   |   |   |           |   |   |           |       |       |       |
    +---+---+   +   +   +   +---+   +   +---+   +---+---+---+   +---+   +---+   +   +
    |   |           |       |   |   |       |           |           |           |   |
    +   +---+   +---+---+   +   +---+   +---+   +---+---+   +   +   +   +---+   +---+
    |               |               |       |       |       |   |   |   |           |
    +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+

```{code-cell} ipython3

```

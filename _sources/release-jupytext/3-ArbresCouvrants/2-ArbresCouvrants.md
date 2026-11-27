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

# Arbres couvrants, algorithmes de Kruskal et Prim

+++ {"deletable": false, "editable": false}

## Sous graphes et graphes partiels

:::{admonition} Définition

On dit qu'un graphe $G'$ est un ***graphe partiel*** d'un
graphe $G=(N;E)$ s'il a les même sommets que $G$ mais ses arêtes
forment un sous ensemble de celles de $G$. Formellement, $G'$ est de
la forme $(N; F)$ avec $F\subset E$.

::::

:::{admonition} Notes
- On parle parfois aussi de ***graphe couvrant***.
- Ne pas confondre avec la notion de *sous-graphe* où l'on a aussi un
  sous ensemble des sommets.  
:::

+++ {"deletable": false, "editable": false}

:::{admonition} Définition
Étant donné un graphe $G=(N;E)$, on appelle ***arbre
couvrant*** de $G$ un graphe $T=(N;F)$ tel que :
- $T$ est un arbre;
- $T$ est un graphe partiel de $G$.
:::

Intuitivement : $T$ est construit avec les arêtes $U$ de $G$ en
connectant ("couvre") tous les sommets de $N$.

+++ {"deletable": false, "editable": false}

::::::{admonition} Exemples

Voici deux graphes avec un arbre couvrant chacun:
:::::{grid}
::::{grid-item}
:::{image} media/4x4_grid_spanning_tree.svg
:::
::::
::::{grid-item}
:::{image} media/Minimum_spanning_tree.svg
:::
::::
:::::
::::::

+++ {"deletable": false, "editable": false}

:::{admonition} Proposition 5

Un graphe $G=(N;E)$ admet un arbre couvrant si et seulement si il est connexe.

:::

+++ {"deletable": false, "editable": false}

:::{admonition} Démonstration

Le sens direct est évident: si $G$ admet un graphe partiel connexe
alors $G$ est connexe.

On prouve la réciproque avec l'algorithme suivant :

    on pose T := G
    tant que que T admet un cycle C
        // Invariant : T est un graphe partiel connexe de G
        supprimer dans T une arête du cycle C
    renvoyer T

En effet, supprimer une arête d'un cycle d'un graphe, ne change pas sa
connexité (pourquoi ?). En conséquence quand ou sort de la boucle, `T`
contient un graphe partiel connexe et sans cycle de G.

:::

+++ {"deletable": false, "editable": false}

:::{note} 

L'algorithme ci dessus n'est pas efficace. On verra ci-dessous deux
algorithmes plus efficaces, dûs à Kruskal et Prim.

:::

+++ {"deletable": false, "editable": false}

:::{admonition} Exercice
1.  Implantez l'algorithme ci-dessus.
2.  Vérifiez sur tous les exemples de graphes connexes que le résultat
    est bien un arbre.
:::

+++ {"deletable": false, "editable": false}

::::{admonition} Exercice

Combien d’arbres couvrants différents possède chacun des graphes ci-dessous?

:::{figure} media/arb-000.jpg
:width: 40%
:::
::::

+++ {"deletable": false, "editable": false}

## Arbre couvrant de poids minimum

Soit $G$ un graphe où l'on a mis un poids sur les arêtes. 

:::{admonition} Tâche: arbre couvrant de poids minimum

La tâche de l'***arbre couvrant de poids minimum*** consiste
à trouver un arbre couvrant dont la somme des poids $c(e)$ des arêtes
est minimum.

:::

+++ {"deletable": false, "editable": false}

:::{attention}

Ne pas confondre :
- arbre couvrant de poids minimum (MST, Minimum Spanning Tree) :
  minimise la *somme des poids* des arêtes
- arbre des plus courts chemins (SPT, Shortest Paths Tree) construit
  par exemple par BFS (Breadth First Search) ou Dijsktra : minimise la
  *distance de la racine à chaque sommet*

:::

+++ {"deletable": false, "editable": false}

::::::{admonition} Exemples
Voici deux arbres couvrants (en rouge). Le premier est de poids $14$,
le deuxième de poids $10$.

:::::{grid}
::::{grid-item}
:::{image} media/tree-022.jpg
:::
::::
::::{grid-item}
:::{image} media/tree-023.jpg
:::
::::
:::::
::::::

+++ {"deletable": false, "editable": false}

Il y a deux algorithmes classiques pour calculer un arbre couvrant de
poids minimum:
- l'algorithme de Kruskal qui procède par ajouts successifs d'arêtes
- l'algorithme de Prim qui procède par ajouts successifs de sommets

Ces deux algorithmes sont dits [***gloutons***](https://fr.wikipedia.org/wiki/Algorithme_glouton) : à chaque
étape ils font une optimisation locale en espérant -- ce qui est le cas ici --
que le résultat soit globalement optimal (un glouton mange immédiatement
tout ce qui lui passe à portée, sans chercher à anticiper).

+++ {"deletable": false, "editable": false}

:::{admonition} Algorithme de Kruskal

**Idée** : On part du graphe $T=(N, \emptyset)$ et on ajoute tour à
tour la nouvelle arête de plus petit poids qui ne crée pas de cycles
(i.e. qui connecte deux composantes connexes différentes).

**Invariant** : à l'étape $i$, le graphe $T$ est acyclique avec $i$
arêtes de poids minimal.

**Références** :
- [Algorithme de Kruskal](https://fr.wikipedia.org/wiki/Algorithme_de_Kruskal)
- [Union Find](https://fr.wikipedia.org/wiki/Union-find)

:::

+++ {"deletable": false, "editable": false}

:::{admonition} Algorithme de Prim

**Idée** : On du graphe $T=(\{n\}, \emptyset)$ et on ajoute tour à
tour chaque sommet en le connectant aux autres par l'arête de poids
minimum.

**Invariant** : Le graphe $T=(U,F)$ est toujours l'arbre couvrant de
poids minimal sur $U\subset N$.

**Références** :
- [Algoritme de Prim](https://fr.wikipedia.org/wiki/Algorithme_de_Prim)
- [File de priorité](https://fr.wikipedia.org/wiki/File_de_priorit%C3%A9)

:::

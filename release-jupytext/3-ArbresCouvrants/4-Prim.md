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

# Étude de l'algorithme de Prim

+++ {"deletable": false, "editable": false}

Avant de mettre en oeuvre l'algorithme de Kruskal, ce qui va nécessiter d'introduire une nouvelle structure de données, regardons rapidement l'algorithme de Prim.

## Principe

L'algorithme de Prim est très similaire à l'algorithme de Dijkstra qui calcule un plus court chemin depuis un sommet source : à partir d'un sommet source (choisi de façon arbitraire), "Prim" effectue un parcours en largeur, pour ajouter successivement de façon vorace (algorithme glouton), les sommets extrémités d'arêtes de poids minimal, en évitant de créer un cycle avec les sommets préalablement choisis.

Cette dernière condition est assurée par le choix d'une _arête compatible_ (ou _sûre_) selon le "propriété de la coupe" (présentée en cours).

De façon imagée, _Prim fait bien pousser l'arbre à partir de sa racine-source_.

+++

## Invariant 

Avant une itération de l'algorithme, notons :

- `S'` l'ensemble des sommets atteints et
- `T` l'ensemble des arêtes retenues. 

À chaque itération :

1. `T` est un arbre couvrant `S'`.
    - Il est connexe et sans cycle, avec `|T| = |S'| − 1`.
2. `T` est contenu dans un arbre couvrant de poids minimum de `G`.
   - Ainsi `T` est "extensible" en un ACM.

Pour un graphe non connexe, l'invariant vaut pour chaque composante, et on obtient une forêt.

+++

**Remarque.** 

Avec ces notations, la propriété de la coupe s'écrit :

- la coupe `(S', V∖S')` est une partition qui respecte `T`, car aucune arête de `T` ne la traverse ;
- `(u, v)` est une arête de poids minimum qui traverse cette coupe ;
- elle est donc compatible (ou sûre) pour `T`.

+++ {"deletable": false, "editable": false}

::::::{admonition} Exercice

Voilà deux graphes auxquels vous allez appliquer _à la main_ l'algorithme de Prim.

    :::::{grid} 2 2 2 2
    ::::{grid-item}
    :::{image} media/arb-001.jpg
    :::
    ::::
    ::::{grid-item}
    :::{image} media/arb-002.jpg
    :::
    ::::
    :::::

1. Quelle est la taille de l'arbre couvrant à construire ?

2. Appliquez l'algorithme _à la main_ et calculez un arbre couvrant de poids minimal.

    - Vous pourrez choisir le sommet '1' comme source.
    - Précisez si vous avez effectué des choix arbitraires -- en plus du sommet-source.
    - Exhibez les états successifs des structures de données (abstraites) de l'algorithme. 
    - Donnez le poids de l'arbre couvrant obtenu.

4. Implémentation : reprenez votre version de l'algorithme de Dijkstra (pour le plus court chemin issu d'un sommet) et modifiez-le pour obtenir une mise en oeuvre de algorithme de Prim.

5. Mettre à jour, si besoin, la fonction qui retourne l'arbre ainsi construit et son poids.

6. Vérifiez votre mise en oeuvre sur les graphes testés à la main.

::::::

+++

## Complexité

Comme pour l'algorithme de Dijkstra, la complexité dépend de l'implantation de la file de priorité (FP) et de la représentation du graphe.

Au pire, la file de priorité contient les $n$ sommets de $G$ et les arêtes candidates sont au plus $m$, le nombre d'arêtes. La suite de l'analyse dépend des coûts d'accès et de modification de la FP, ainsi que la recherche d'une arête candidate.  

En utilisant un tas binaire et une liste d'adjacence, l'algorithme de Prim est de complexité :
$O((m + n)\log(n))$,
où $m$ est le nombre d'arêtes et $n$ le nombre de sommets du graphe.

Avec des vecteurs (ou des listes) et une matrice d'adjacence, la complexité devient quadratique en $n$.

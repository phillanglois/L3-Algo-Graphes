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

+++ {"deletable": false, "editable": false, "grade_id": "cell-5e08e1c92ff0dc4a", "tags": ["locked"]}

# Implantation

+++ {"deletable": false, "editable": false, "grade_id": "cell-c5e7379aa4f69a00", "tags": ["locked"]}

## Exemples Python sur les dictionnaires et compréhensions

:::{admonition} Exercice
Analysez les exemples suivants:
:::

```{code-cell} ipython3
l = [3,2,1,0]
[ i**2  for i in l ]
```

```{code-cell} ipython3
l = ["a", "z", "b"]
d = {l[i] : i for i in range(len(l))}
```

```{code-cell} ipython3
for v in d.keys():
    print(v)
```

```{code-cell} ipython3
[(v, 1) for v in l]
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-5021bc62f52ac35b", "tags": ["locked"]}

## Conversions

+++ {"deletable": false, "editable": false, "grade_id": "cell-5b815c23a7f6fe12", "tags": ["locked"]}

:::{admonition} Exercice
Choisissez une des structures de données de graphes que l'on a vues (liste d'arêtes,
dictionnaire des voisins, dictionnaire d'arêtes, matrice d'adjacence), ou une autre.

Implantez ci-dessous des fonctions Python `from_matrix`, `from_edges`,
`from_neighbor_dict`, `from_edge_dict`. Par exemple, la fonction `from_matrix` prendra un
graphe représenté par une matrice d'adjacence et renverra le même graphe dans la
structure de donnée que vous avez choisi.

Testez systématiquement ces fonctions -- avec des tests automatiques -- sur les exemples
de la fiche précédente.
:::

```{code-cell} ipython3
:deletable: false
:grade_id: cell-7465315001846df2
:points: 0
:tags: [answer]

# Cellule cell-7465315001846df2
# REMPLACEZ TOUTE CETTE LIGNE PAR VOTRE CODE

# G0

#EdgeList
L0 = [ (0,1,10), (0,2,4) ] 

#AdjacencyMatrix
M0 = [ [0, 10, 4],
       [0,  0, 0],
       [0,  0, 0]
     ] 

#EdgeDict
DA0 = { (0,1): 10,
        (0,2): 4 }

# NeighborDict
DV0 = { 0: [(1,10), (2,4) ], 1: [], 2: [] }

assert from_matrix(M0) == DV0 
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-a43fd9e023098145", "tags": ["locked"]}

## Une classe graphe

+++ {"deletable": false, "editable": false, "grade_id": "cell-e1a35d7c120ff727", "tags": ["locked"]}

:::{admonition} Exercice
Le fichier [graph.py](graph.py) contient un squelette de classe pour représenter des
graphes. Votre mission est de compléter les méthodes non implantées avant la prochaine
séance, en vous appuyant sur la documentation, les commentaires et les tests.

Le [rapport](Rapport.md) contient des vérifications automatiques pour votre code.
Utilisez le au fur et à mesure pour suivre votre avancement et complétez le.
:::

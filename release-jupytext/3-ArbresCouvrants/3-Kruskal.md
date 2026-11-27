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

# Étude de l'algorithme de Kruskal

+++ {"deletable": false, "editable": false}

Dans ce qui suit nous exécutons pas à pas, l'algorithme de Kruskal :

```{code-cell} ipython3
:deletable: false
:editable: false

from graph import Graph, examples
import networkx
import matplotlib
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
:deletable: false
:editable: false

## On part d'un graphe valué et on fixe un dessin
G = examples.cours_1_reseau()
GNX = G.networkx()
layout = networkx.planar_layout(GNX)
edges_weight = {(u, v) : w for u, v, w in G.edges()}
```

```{code-cell} ipython3
:deletable: false
:editable: false

## On visualise la progression de l'algorithme en affectant à chaque arête un état représenté par une couleur

from enum import Enum, unique
@unique
class Status(Enum):
    AFAIRE = 0
    GARDEE = 1
    SUPRIMEE = 2
    ENCOURS = 3
colors_code = { 
    Status.AFAIRE : 'black',
    Status.GARDEE : 'green',
    Status.SUPRIMEE : 'lightgray',
    Status.ENCOURS : 'red'
}
```

```{code-cell} ipython3
:deletable: false
:editable: false

def show_kruskal(status):
    plt.figure()
    colors = [colors_code[status[u,v]] for (u, v) in GNX.edges()]
    networkx.draw(GNX, layout, edge_color = colors, width=3, linewidths=1,
                  node_size=500, node_color = 'lightgray', alpha=0.9,
                  labels = {node : node for node in G.nodes()})
    networkx.draw_networkx_edge_labels(GNX, layout, edge_labels= edges_weight, font_color='black')
    plt.axis('off')
    plt.show()
```

```{code-cell} ipython3
:deletable: false
:editable: false

# Au début toutes les arêtes sont marquée "à faire"
edges_status = {(u, v) : Status.AFAIRE for u, v, _ in G.edges()}
show_kruskal(edges_status)
```

```{code-cell} ipython3
:deletable: false
:editable: false

# On choisit l'une des arêtes de poids minimum
edges_status["F", "G"] = Status.ENCOURS
show_kruskal(edges_status)
```

```{code-cell} ipython3
:deletable: false
:editable: false

# Elle ne crée pas de cycle. On la garde
edges_status["F", "G"] = Status.GARDEE
show_kruskal(edges_status)
```

```{code-cell} ipython3
:deletable: false
:editable: false

# On choisit l'une des arêtes de poids minimum
edges_status["B", "C"] = Status.ENCOURS
show_kruskal(edges_status)
```

```{code-cell} ipython3
:deletable: false
:editable: false

# Elle ne crée pas de cycle. On la garde
edges_status["B", "C"] = Status.GARDEE
show_kruskal(edges_status)
```

```{code-cell} ipython3
:deletable: false
:editable: false

# L'algorithme se continue ainsi
edges_status["B", "G"] = Status.ENCOURS
show_kruskal(edges_status)
edges_status["B", "G"] = Status.GARDEE
edges_status["A", "G"] = Status.ENCOURS
show_kruskal(edges_status)
edges_status["A", "G"] = Status.GARDEE
edges_status["C", "H"] = Status.ENCOURS
show_kruskal(edges_status)
edges_status["C", "H"] = Status.GARDEE
edges_status["E", "G"] = Status.ENCOURS
show_kruskal(edges_status)
edges_status["E", "G"] = Status.GARDEE
show_kruskal(edges_status)
```

```{code-cell} ipython3
:deletable: false
:editable: false

# On Passe maintenant aux arêtes de poids 3
edges_status["E", "F"] = Status.ENCOURS
show_kruskal(edges_status)
```

```{code-cell} ipython3
:deletable: false
:editable: false

# L'arête E - F crée un Cycle, on la supprime
edges_status["E", "F"] = Status.SUPRIMEE
show_kruskal(edges_status)
```

```{code-cell} ipython3
:deletable: false
:editable: false

# On Passe maintenant a A - B
edges_status["A", "B"] = Status.ENCOURS
show_kruskal(edges_status)
```

```{code-cell} ipython3
:deletable: false
:editable: false

# L'arête A - B crée un Cycle, on la supprime
edges_status["A", "B"] = Status.SUPRIMEE
show_kruskal(edges_status)
```

```{code-cell} ipython3
:deletable: false
:editable: false

# Idem pour E - H
edges_status["E", "H"] = Status.SUPRIMEE
show_kruskal(edges_status)
```

```{code-cell} ipython3
:deletable: false
:editable: false

# L'algorithme se poursuit
edges_status["A", "F"] = Status.ENCOURS
show_kruskal(edges_status)
edges_status["A", "F"] = Status.SUPRIMEE
edges_status["C", "D"] = Status.ENCOURS
show_kruskal(edges_status)
edges_status["C", "D"] = Status.GARDEE
edges_status["G", "H"] = Status.ENCOURS
show_kruskal(edges_status)
edges_status["G", "H"] = Status.SUPRIMEE
show_kruskal(edges_status)
```

```{code-cell} ipython3
:deletable: false
:editable: false

# On pourrait continuer jusqu'à ce que l'on ai vu toutes les arêtes...
# On remarque que l'on a choisi 7 arêtes dans un graphe à 8 sommets. On peut donc s'arrêter dès maintenant.
edges_status["C", "G"] = Status.SUPRIMEE
edges_status["D", "E"] = Status.SUPRIMEE
edges_status["D", "H"] = Status.SUPRIMEE
show_kruskal(edges_status)
```

+++ {"deletable": false, "editable": false}

On a calculé un arbre couvrant de poids 13 du graphe.

+++ {"deletable": false, "editable": false}

L'invariant de l'algorithme est le suivant : *à chaque étape, le
graphe des arêtes choisies est un graphe partiel acyclique de $G$ de
poids minimum*.

+++ {"deletable": false, "editable": false}

::::::{admonition} Exercice

1.  Appliquez à la main l'algorithme de Kruskal aux deux graphes
    suivants. On donnera un arbre couvrant de **poids minimal** et un
    arbre couvrant de **poids maximal**. Pour ce dernier on applique
    le même algorithme mais en choissant un arête de plus fort poids.
	Donnez le poids de l'arbre couvrant obtenu.

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

3.  Expliquez pourquoi l'invariant est conservé.


::::::

```{code-cell} ipython3

```

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

# Plus courts chemins, avec poids de signe quelconque : l'[algorithme de Bellman-Ford](https://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford)

+++

On a vu en cours l'algorithme de Bellman-Ford qui applique le principe de programmation dynamique au calcul des plus courts chemins d'une source donnée aux sommets d'un graphe avec poids positifs et négatifs. On rappelle que la validité de cette solution impose l'absence dans le graphe de cycle de poids total négatif.

+++ {"deletable": false, "editable": false}

:::{admonition} Exercice

1. Ecrire dans un fichier python, la fonction `bellman_ford` décrite dans la cellule suivante. 
2. Vérifier votre algorithme avec l'exemple résolu en cours.
3. Instrumenter votre code pour vérifier chaque itération de cette résolution. La vérifier par rapport à l'exemple du cours. 
4.  Appliquez cette fonction au graphe `G` ci-dessous -- déjà traité avec l'algorithme de Dijkstra.

:::

```{code-cell} ipython3
from typing import Dict, Tuple, Optional
from graph import Graph, Node

infinity = float("inf")

def bellman_ford(
    G: Graph,
    e: Node
) -> Tuple[Dict[Node, float], Dict[Node, Optional[Node]]]:
    """
    Applique l'algorithme de Bellman-Ford à G en partant de e.

    Renvoie :
      - un dictionnaire associant à chaque sommet sa distance depuis e ;
      - un dictionnaire associant à chaque sommet v un autre sommet
        d'où vient l'un des chemins les plus courts de e à v.

    Les distances des sommets non accessibles depuis e valent inf.

    Lève ValueError si un circuit de poids strictement négatif
    est accessible depuis e.
    """
    
    ### BEGIN SOLUTION
    nodes = G.nodes()
    n = len(nodes)

    if e not in nodes:
        raise ValueError("Le sommet de départ n'appartient pas au graphe.")

    # Initialisation
    dist = {v: float('inf') for v in nodes}
    pred = {v: None for v in nodes}

    dist[e] = 0.0

    # Phase de relaxation : au plus n-1 itérations
    for _ in range(n - 1):
        changement = False

        for v in nodes:
            # On examine les arêtes entrantes dans v
            for u in G.predecessors(v):

                poids = G.capacity(u, v)

                # Relaxation de l'arête (u, v)
                if dist[u] != float('inf') and \
                   dist[u] + poids < dist[v]:

                    dist[v] = dist[u] + poids
                    pred[v] = u
                    changement = True

        # Arrêt anticipé si aucune distance n'a été modifiée
        if not changement:
            break

    # Détection d'un circuit de poids négatif accessible depuis e
    for v in nodes:
        for u in G.predecessors(v):

            poids = G.capacity(u, v)

            if dist[u] != float('inf') and \
               dist[u] + poids < dist[v]:

                raise ValueError(
                    "Le graphe contient un circuit de poids négatif "
                    "accessible depuis le sommet de départ."
                )

    return dist, pred
    ### END SOLUTION
```

+++ {"deletable": false, "editable": false}

Comme précédemment, on considère le graphe suivant qui modélise un réseau routier :
% By HB (Own work) [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], via Wikimedia Commons
% <img src="media/DijkstraBis01.svg">

```{code-cell} ipython3
%load_ext autoreload
%autoreload 2
from graph import examples
from dijkstra import *
```

```{code-cell} ipython3
:deletable: false
:editable: false

G = examples.dijkstra()
G.show()
```

+++ {"deletable": false, "editable": false}

On souhaite calculer le plus court chemin entre deux sommets de ce graphe.

```{code-cell} ipython3
:deletable: false

# REPLACE THIS WHOLE LINE BY YOUR CODE
```

+++ {"deletable": false, "editable": false}

:::{admonition} Exercice, suite

3.  Déduisez en la distance entre `A` et `J`, à mettre dans la
    variable `distance_AJ`:

:::

```{code-cell} ipython3
:deletable: false

# REPLACE THIS WHOLE LINE BY YOUR CODE
```

```{code-cell} ipython3
:deletable: false
:editable: false

# Vérifie votre résultat sans dévoiler la solution, par la magie des fonctions de hachage :-)
import hashlib
assert hashlib.md5(bytes(distance_AJ)).hexdigest() == '2f6064003b888e403627e493532fc751'
```

```{code-cell} ipython3
:deletable: false
:editable: false

distances = bellman_ford(G, "A")[0]
assert distances["A"] == 0
```

```{code-cell} ipython3
:deletable: false
:editable: false

assert sum(distances.values()) == 2774
```

+++ {"deletable": false, "editable": false}

:::{admonition} Exercice, fin

4.  Ecrire une nouvelle version de la fonction `shortest_path` qui retourne le plus court chemin entre deux noeuds `u` et `v`, cette fois  calculé par `bellman-ford`.
5.  L'utiliser pour calculer un plus court chemin entre `A` et `J` dans `G`.

:::

```{code-cell} ipython3
:deletable: false

# REPLACE THIS WHOLE LINE BY YOUR CODE
```

+++ {"deletable": false, "editable": false}

::::{admonition} Problème 1 : le retour du trajet le plus rapide en métro de Montgallet à Billancourt ?

<center>

:::{image} ../media/metro-paris.gif
:width: 50%
:alt: Le plan du métro de Paris
:::

</center>

Reprenez les développements du notebook précédent et 
utilisez la fonction `bellman_ford` retrouver un plus court chemin de Montgallet à Billancourt! Vous stockerez encore la longueur de ce chemin dans dans la variable `distance`.

::::

```{code-cell} ipython3
:deletable: false

# REPLACE THIS WHOLE LINE BY YOUR CODE
```

```{code-cell} ipython3
:deletable: false

# REPLACE THIS WHOLE LINE BY YOUR CODE
```

```{code-cell} ipython3
:deletable: false
:editable: false

# Vérifie votre résultat sans dévoiler la solution, par la magie des fonctions de hachage :-)
import hashlib
assert hashlib.md5(bytes(int(distance))).hexdigest() == '47699f4b69b37670eb6ce45276ad9a30'
```

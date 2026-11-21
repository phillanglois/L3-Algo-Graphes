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

# Plus courts chemins, avec poids de signe quelconque : algorithmes de [Bellman-Ford](https://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford) et de [Floyd-Warshall](https://fr.wikipedia.org/wiki/Algorithme_de_Floyd-Warshall)


Voici deux algorithmes de plus courts chemins (PCC), dans un graphe avec poids de signe quelconque, qui appliquent le principe de la [programmation dynamique](https://fr.wikipedia.org/wiki/Programmation_dynamique).

On rappelle que la validité de cette solution impose l'absence dans le graphe de cycle de poids total négatif.

- L'_algorithme de Bellman-Ford_, comme celui de Dijkstra, calcule un PCC d'une source donnée aux sommets d'un graphe.
- L'_algorithme de Floyd-Warshall_ calcule des plus courts chemins _de toute paire de sommets_ d'un graphe.

```{code-cell} ipython3
:deletable: false
:editable: false

from typing import Dict, Tuple, Optional
from graph import Graph, Node

infinity = float("inf")
```

+++ {"deletable": false, "editable": false}

## [Algorithme de Bellman-Ford]((https://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford))

Soit donc un PCC d'une source donnée vers tous les sommets. 
Se référer si besoin à la page wikipedia dans le titre de cette section.


:::{admonition} Exercice

1. Ecrire (dans un fichier python), la fonction `bellman_ford` décrite dans la cellule suivante. 
2. Vérifier votre algorithme avec l'exemple résolu en cours : 
3. Instrumenter votre code pour vérifier chaque itération de cette résolution. La vérifier par rapport à l'exemple du cours `examples.grandcolas_bf()`.
4. Ecrire une nouvelle version de la fonction `shortest_path` qui retourne un plus court chemin entre deux noeuds `u` et `v`, cette fois  calculé par `bellman-ford`.
5.  L'utiliser pour calculer un plus court chemin de `s` à `b` dans `G`.
:::

```{code-cell} ipython3
:deletable: false
:editable: true

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
    raise NotImplementedError() # REPLACE THIS WHOLE LINE BY YOUR CODE
```

```{code-cell} ipython3
:deletable: false
:editable: true

def shortest_path(graph: Graph, u: Node, v: Node) -> Tuple[list[Node], float]:
    "Bellman-Ford pour renvoyer un plus court chemin de `u` à `v`, ainsi que sa longueur"
    raise NotImplementedError() # REPLACE THIS WHOLE LINE BY YOUR CODE
```

```{code-cell} ipython3
:deletable: false
:editable: false

%load_ext autoreload
%autoreload 2
from graph import examples
```

```{code-cell} ipython3
:deletable: false
:editable: true

import hashlib

G = examples.grandcolas_bf()
G.show()

# REPLACE THIS WHOLE LINE BY YOUR CODE
```

+++ {"deletable": false, "editable": false}

### Le métro parisien : seconde !

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
:editable: true

# REPLACE THIS WHOLE LINE BY YOUR CODE
```

```{code-cell} ipython3
:deletable: false
:editable: true

# REPLACE THIS WHOLE LINE BY YOUR CODE
```

```{code-cell} ipython3
:deletable: false
:editable: true

# REPLACE THIS WHOLE LINE BY YOUR CODE
```

```{code-cell} ipython3
:deletable: false
:editable: true

# REPLACE THIS WHOLE LINE BY YOUR CODE
```

+++ {"deletable": false, "editable": false}

## [Algorithme de Floyd-Warshall](https://fr.wikipedia.org/wiki/Algorithme_de_Floyd-Warshall)


Soit donc des PCC de toute paire de sommets d'un graphe.
Se référer si besoin à la page wikipedia dans le titre de cette section.

:::{admonition} Exercice

1. Ecrire (dans un fichier python), la fonction `floyd_warshall` décrite dans la cellule suivante.
**Indication.** Une première version pourra se dispenser du traitement de la construction des pcc calculés. La compléter dans un second temps. 
1. Vérifier votre algorithme avec l'exemple résolu en cours.
2. Ecrire une nouvelle version de la fonction `shortest_path` qui retourne le plus court chemin entre deux noeuds `u` et `v` à partir du calcul `floyd_warshall`. 
3.  De façon similaire à la section précédente (Bellman-Ford), vérifier avec le plus court chemin entre `A` et `J` dans `G`.
:::

```{code-cell} ipython3
:deletable: false
:editable: true

def floyd_warshall(G: Graph) -> Tuple[Dict[Tuple[Node], float], Dict[Tuple[Node, Node], Optional[Node]]]:
    """
    Applique l'algorithme de Floyd-Warshall.

    Renvoie :
      - un dict associant à chaque paire de sommets, sa distance (ppc);
      - un dict associant à chaque paire de sommets d'où vient l'un des chemins les plus courts :
        le premier pas (sommet suivant) pour aller de i à j
        
    Les distances des sommets non accessibles valent inf.

    Lève ValueError si un circuit de poids strictement négatif.
    """
    raise NotImplementedError() # REPLACE THIS WHOLE LINE BY YOUR CODE
```

+++ {"deletable": false, "editable": false}

2. Vérification avec exemple du cours

```{code-cell} ipython3
:deletable: false
:editable: true

G = examples.grandcolas_bf()
# REPLACE THIS WHOLE LINE BY YOUR CODE
```

+++ {"deletable": false, "editable": false}

3. `shortest_path` avec Floyd-Warshall

```{code-cell} ipython3
:deletable: false
:editable: true

def shortest_path(graph: Graph, u: Node, v: Node) -> Tuple[list[Node], float]:
    "Floyd-Warshall pour renvoyer les plus courts chemin de paires de sommets`u` à `v`, ainsi que sa longueur"
    raise NotImplementedError() # REPLACE THIS WHOLE LINE BY YOUR CODE
```

+++ {"deletable": false, "editable": false}

4. Application

```{code-cell} ipython3
:deletable: false
:editable: true

# REPLACE THIS WHOLE LINE BY YOUR CODE
```

+++ {"deletable": false, "editable": false}

### Le métro parisien : troisième !

Reprendre l'exercice du métro parisien avec cette approche.  

- Quelle est la taille des résultats calculés par cette approche ?
- Retrouver les résultats du trajet "Montgallet -Billancourt"
- Comparer sur cet exemple, les temps d'exécution des approches "Dijkstra", "Bellman-Ford" et "Floyd-Warshall".
- Qu'en penser ?

```{code-cell} ipython3
:deletable: false
:editable: true

# REPLACE THIS WHOLE LINE BY YOUR CODE
```

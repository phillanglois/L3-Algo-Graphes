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

# Plus courts chemins, avec poids: l'[algorithme de Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra)

+++ {"deletable": false, "editable": false}

On considère le graphe suivant qui modélise un réseau routier :
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

+++ {"deletable": false, "editable": false}

:::{admonition} Exercice

1.  Complétez la fonction `dijkstra` du fichier [dijkstra.py](dijkstra.py).
2.  Appliquez cette fonction au graphe `G` ci-dessus:

:::

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

distances = dijkstra(G, "A")[0]
assert distances["A"] == 0
```

```{code-cell} ipython3
:deletable: false
:editable: false

assert sum(distances.values()) == 2774
```

+++ {"deletable": false, "editable": false}

:::{admonition} Exercice, suite

4.  Implantez la fonction `shortest_path` dans [dijkstra.py](dijkstra.py), et utilisez là pour calculer un plus court chemin entre `A` et `J` dans `G`:

:::

```{code-cell} ipython3
:deletable: false

# REPLACE THIS WHOLE LINE BY YOUR CODE
```

+++ {"deletable": false, "editable": false}

:::{admonition} Exercice, suite

5.  Pour aller plus loin : Instrumentez votre fonction pour en visualiser l'exécution.

:::

+++ {"deletable": false, "editable": false}

::::{admonition} Problème 1: le trajet le plus rapide en métro de Montgallet à Billancourt ?

<center>

:::{image} media/metro-paris.gif
:width: 50%
:alt: Le plan du métro de Paris
:::

</center>

1. Le fichier [metro_complet.txt](metro_complet.txt) contient la description d'un graphe modélisant le métro de Paris. Consultez son contenu pour en comprendre le format.
2. Implantez une fonction qui lit le fichier et renvoie le graphe qu'il contient sous la forme d'un objet de type `Graph`.
3. Utilisez la fonction `dijkstra` pour calculer un plus court chemin de Montgallet à Billancourt! Vous stockerez la longueur de ce chemin dans dans la variable `distance`.

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

```{code-cell} ipython3

```

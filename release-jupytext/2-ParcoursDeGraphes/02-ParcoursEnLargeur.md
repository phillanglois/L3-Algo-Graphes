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

# [Parcours en largeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur) et calcul de distances

+++ {"deletable": false, "editable": false}

Dans cette feuille, nous raffinons l'algorithme de parcours de graphe
vu précédemment pour calculer des *distances simples* entre sommets
d'un graphe, ne tenant pas compte des poids des arêtes. Nous suivons
la même démarche que pour notre premier algorithme: invariants, test
sur des exemples, visualisation, complexité, preuve de correction.

+++ {"deletable": false, "editable": false}

:::{admonition} Définition : *distance simple* dans un graphe

La *distance* entre deux sommets $u$ et $v$ d'un graphe $G$ est le
plus petit entier $l$ tel qu'il existe un chemin avec $l$ arêtes
allant de $u$ à $v$. S'il n'y a pas de tel chemin, alors la distance
est $\infty$.

:::

+++ {"deletable": false, "editable": false}

**Exercice :**

+++ {"deletable": false, "editable": false}

1. Complétez la fonction suivante qui implante un parcours en largeur,
   en vous laissant guider par les invariants fournis:

```{code-cell} ipython3
from graph import Graph, Node
from typing import Dict
```

```{code-cell} ipython3
:deletable: false

def parcours_en_largeur(G: Graph, u: Node) -> Dict[Node, int]:
    """
    INPUT:
    - 'G' - un graphe
    - 'u' - un sommet du graphe
    
    OUTPUT: un dictionnaire associant à chaque sommet `v` accessible depuis `u` sa distance depuis `u`
    """
    distances = {u: 0} # L'ensemble des sommets déjà rencontrés
    todo      = [u]    # Une liste de sommets à traiter
    
    while todo:
        # Invariants:
        # - Si `v` est dans `distance`, alors il y a un chemin de `u` à `v`,
        #   et distance[v] contient la distance de `u` à `v`;
        # - Si `v` est dans `distance` et pas dans `todo`
        #   alors tous les voisins de `v` sont dans `distance`
        raise NotImplementedError() # REPLACE THIS WHOLE LINE BY YOUR CODE
    return distances
```

+++ {"deletable": false, "editable": false}

2. Testez que votre fonction est correcte sur les exemples suivants.
   Si elle ne l'est pas, utilisez la question suivante pour déboguer!

```{code-cell} ipython3
:deletable: false
:editable: false

from graph import Graph, examples
```

```{code-cell} ipython3
:deletable: false
:editable: false

C3 = examples.C3()
C3.edges()
```

```{code-cell} ipython3
:deletable: false
:editable: false

assert parcours_en_largeur(C3, 0) == {0: 0, 1: 1, 2: 2}
```

```{code-cell} ipython3
:deletable: false
:editable: false

T3 = examples.T3()
T3.edges()
```

```{code-cell} ipython3
:deletable: false
:editable: false

assert parcours_en_largeur(T3, 0) == {0: 0, 1: 1, 2: 1}
```

```{code-cell} ipython3
:deletable: false
:editable: false

from graph import examples
G = examples.parcours_directed()
```

```{code-cell} ipython3
:deletable: false
:editable: false

assert parcours_en_largeur(G, "H") == {'H': 0, 'F': 1, 'G': 2}
```

```{code-cell} ipython3
:deletable: false
:editable: false

assert parcours_en_largeur(G, "A") == {'A': 0, 'B': 1, 'G': 1, 'F': 1, 'C': 2, 'H': 2, 'D': 3}
```

+++ {"deletable": false, "editable": false}

3. Instrumentez votre code comme dans la feuille précédente pour visualiser son exécution

```{code-cell} ipython3

```

+++ {"deletable": false}

::::{admonition} Exercice : Complexité

Donnez une borne de complexité pour votre implantation de l'algorithme `parcours_en_largeur`. Comme précédemment, vous donnerez le modèle de complexité, le coût de vos opérations, et vous argumenterez.

:::{admonition} Pour aller plus loin
:class: hint

Pour simplifier, nous avons utilisé une liste pour `todo`. Pour
avoir une bonne complexité, il faudrait utiliser une *file* (FIFO),
typiquement implantée au moyen d'une liste chaînée et non un tableau
comme dans les listes Python. Voir par exemple `queue.SimpleQueue`.

:::


% REPLACE THIS LINE BY YOUR ANSWER

::::

+++ {"deletable": false, "editable": false}

::::{admonition} Exercice : pour aller plus loin

Chronométrez votre code sur des graphes de taille croissante afin de
tracer une courbe de complexité pratique et vérifier empiriquement que
votre code a la complexité voulue.

:::{admonition} Indication
:class: tip

Vous pouvez par exemple utiliser les outils `time.time`, `%timit`,
`timeit` ou
[bleachermark](https://github.com/miguelmarco/bleachermark) (note : ce
dernier n'est pas encore compatible Python 3).

:::

::::

+++ {"deletable": false}

:::{admonition} Exercice : Preuve de correction

% REPLACE THIS LINE BY YOUR ANSWER

:::

+++ {"deletable": false, "editable": false}

## Conclusion

Dans cette feuille, vous avez mené en toute autonomie l'implantation
et l'étude d'un autre parcours de graphe pour mettre en pratique tout
ce que nous avions vu dans la fiche précédente. Bravo!

Vous pouvez maintenant aborder les [parcours en
profondeur](03-ParcoursEnProfondeur.md).

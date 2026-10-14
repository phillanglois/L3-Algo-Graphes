---
jupytext:
  notebook_metadata_filter: rise
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
rise:
  auto_select: first
  autolaunch: false
  centered: false
  controls: false
  enable_chalkboard: true
  height: 100%
  margin: 0
  maxScale: 1
  minScale: 1
  scroll: true
  slideNumber: true
  start_slideshow_at: selected
  transition: none
  width: 90%
---

+++ {"deletable": false, "editable": false}

# Étude d'un algorithme de parcours de graphes

+++ {"deletable": false, "editable": false}

:::{admonition} Définitions

Soit $G$ un graphe.
- un *chemin* est une suite de sommets $(v_0, v_1, v_2, ...)$ tel qu'il existe une arête entre chaque paire de sommets $v_i$ et $v_{i+1}$
- la *distance* entre deux sommets `u` et `v` est la longueur du plus court chemin entre `u` et `v` (ou la somme des poids des arêtes).
- On suppose ici que $G$ est non orienté. La *composante connexe* d'un sommet $u$ de $G$ est l'ensemble des sommets atteignables depuis $u$ en suivant un chemin dans $G$.

:::

+++ {"deletable": false, "editable": false}

## L'algorithme

+++ {"deletable": false, "editable": false}

L'objectif de cette feuille est d'étudier l'algorithme suivant :

```{code-cell} ipython3
:deletable: false
:editable: false

def parcours(G, u):
    """
    INPUT:
    - 'G' - un graphe
    - 'u' - un sommet du graphe
    
    OUTPUT: la liste des sommets `v` de `G`
            tels qu'il existe un chemin de `u` à `v`
    """
    marked = {u} # L'ensemble des sommets déjà rencontrés
    todo   = {u} # L'ensemble des sommets déjà rencontrés, mais pas encore traités
    
    while todo:
        # Invariants:
        # - Si `v` est dans `marked`, alors il y a un chemin de `u` à `v`
        # - Si `v` est dans `marked` et pas dans `todo`
        #   alors tous les voisins de `v` sont dans dans `marked`
        v = todo.pop()
        for w in G.neighbors(v):
            if w not in marked:
                marked.add(w)
                todo.add(w)
    return marked
```

+++ {"deletable": false, "editable": false}

## Étude sur un exemple

Nous allons commencer par étudier le comportement de cet algorithme sur le graphe suivant :

```{code-cell} ipython3
from graph import examples
G = examples.parcours_directed()
G.show()
```

+++ {"deletable": false, "editable": false}

**Note:** Si votre classe `Graph` n'est pas au point, remplacez `graph` par `graph_networkx` ci-dessus.

+++ {"deletable": false, "editable": false}

:::{admonition} Exercice
1.  Copiez le graphe ci-dessus sur une feuille de papier.
2.  Uniquement en consultant la documentation, prédire quel devrait
    être le résultat de l'algorithme appliqué au graphe ci-dessus avec
    `u="D"`.
3.  Vérifiez en exécutant la fonction `parcours` ci-dessous.
:::

```{code-cell} ipython3
:deletable: false

# REPLACE THIS WHOLE LINE BY YOUR CODE
```

+++ {"deletable": false, "editable": false}

## Tests

```{code-cell} ipython3
:deletable: false
:editable: false

H = examples.cours_1_reseau()
assert parcours(G, "A") == {'A', 'B', 'C', 'D', 'F', 'G', 'H'}
```

```{code-cell} ipython3
:deletable: false
:editable: false

assert parcours(G, "B") == {'B', 'C', 'D', 'F', 'G', 'H'}
```

```{code-cell} ipython3
:deletable: false
:editable: false

H = examples.cours_1_G()
assert sorted(parcours(H, 3)) == [0, 1, 2, 3, 4, 5]
```

```{code-cell} ipython3
:deletable: false
:editable: false

H = examples.disconnected()
assert sorted(parcours(H, 1)) == [1, 2, 5]
assert sorted(parcours(H, 3)) == [3, 4]
```

+++ {"deletable": false, "editable": false}

## Visualisation

+++ {"deletable": false, "editable": false}

Nous allons maintenant visualiser l'exécution de notre algorithme. Pour cela, nous allons:
1.  Instrumenter le code en insérant des observations des variables locales aux endroits clé (comme lorsque l'on débogue avec `print`)/
2.  Définir une visualisation de ses variables locales.

::::{admonition} Exercice

Exécutez les cellules ci-dessous, jusqu'à l'appel à la fonction `parcours`, puis jouez avec la «télécommande» pour exécuter le code pas à pas, revenir en arrière, etc.

:::{attention}
Il y a actuellement un boggue: la visualisation n'est mise à jour que en pas à pas.
:::

::::

```{code-cell} ipython3
:deletable: false
:editable: false

import copy
```

```{code-cell} ipython3
:deletable: false
:editable: false

def parcours_visualisation(G, u):
    """
    INPUT:
    - 'G' - un graphe
    - 'u' - un sommet du graphe
    
    OUTPUT: la liste des sommets `v` de `G`
            tels qu'il existe un chemin de `u` à `v`
    """
    marked = {u} # L'ensemble des sommets déjà rencontrés
    todo   = {u} # L'ensemble des sommets déjà rencontrés, mais pas encore traités
    
    player.player.reset(copy.deepcopy(locals()))
    
    while todo:
        # Invariants:
        # - Si `v` est dans `marked`, alors il y a un chemin de `u` à `v`
        # - Si `v` est dans `marked` et pas dans `todo`
        #   alors tous les voisins de `v` sont dans dans `marked`
        v = todo.pop()
        # Observation des variables locales
        player.set_value(copy.deepcopy(locals()))
        for w in G.neighbors(v):
            
            if w not in marked:
                marked.add(w)
                todo.add(w)
                # Observation des variables locales
                player.set_value(copy.deepcopy(locals()))
        v = None
        # Observation des variables locales
        player.set_value(copy.deepcopy(locals()))
    return marked
```

```{code-cell} ipython3
:deletable: false
:editable: false

import graph_algorithm_player
variables = [{'name': 'G',      'type': 'graph' },
             {'name': 'marked', 'type': 'nodes', 'color': 'green',  'display': True},
             {'name': 'todo',   'type': 'nodes', 'color': 'red',    'display': True},
             {'name': 'v',      'type': 'node',  'color': 'yellow', 'display': True}]
player = graph_algorithm_player.GraphAlgorithmPlayer(variables=variables)
player
```

```{code-cell} ipython3
:deletable: false
:editable: false

parcours_visualisation(G, "A")
```

+++ {"deletable": false, "editable": false}

## Analyse théorique et invariants

+++ {"deletable": false}

:::{admonition} Exercice: Complexité
Majorez la complexité de votre implantation de l'algorithme. Pour cela:
1.  Choisissez un *modèle de complexité*: opération(s) élémentaires et
    métrique(s) pour la taille des données en entrée. 
2.  Considérez combien de fois chaque sommet est manipulé, combien de
    fois chaque arête est manipulée.
3.  Rappelez la complexité des opérations de votre implantation de
    `Graph` qui sont utilisées.
4.  Concluez

% REPLACE THIS LINE BY YOUR ANSWER
:::

+++ {"deletable": false, "editable": false}

L'exercice précédent a confirmé qu'il s'agissait bien d'un algorithme: il termine en un temps fini. Il reste à démontrer qu'il est correct.

+++ {"deletable": false, "editable": false}

Vous avez remarqué les *invariants* marqués en commentaires dans le code. Ce sont des propriétés qui sont sensées être vérifiées à toutes les itérations de la boucle.

+++ {"deletable": false}

:::{admonition} Exercice: Preuve de correction
1. Vérifiez que les invariants sont respectés à l'initialisation.
2. Vérifiez que, à chaque itération de la boucle while, si les invariants sont respectés au début de l'itération, alors ils le sont encore à la fin.
3. Qu'en déduisez vous par récurrence?
4. Concluez en montrant que, s'il y a un chemin de `u` à `v`, alors `v` est dans `marked` à la fin de l'exécution de l'algorithme.

% REPLACE THIS LINE BY YOUR ANSWER

:::

+++ {"deletable": false, "editable": false}

## Conclusion

Dans cette feuille, nous avons étudié un algorithme au moyen de deux outils :
- L'instrumentation du code pour observer visuellement son exécution.
- Les invariants pour démontrer la correction de l'algorithme.

Nous utiliserons systématiquement ces outils dans la suite du cours.

:::{admonition} Invariants
:class: hint
Les invariants sont des outils très puissants pour le programmeur. Ils
jouent le même rôle que les hypothèses de récurences dans les
démonstrations. Ils permettent de se convaincre après coup que les
programmes sont corrects. Au moins aussi important, ce sont des guides
précieux sur lesquels s'appuyer au moment de la programmation elle
même. En fait, bien souvent, une fois que l'on a choisis ses
invariants, l'écriture du programme est quasiment imposée.
:::

:::{admonition} Recommandations
:class: tip
- Écrivez vos programmes dans l'ordre suivant: documentation, tests,
  invariants, puis seulement code.

  C'est l'analogue exact de la démarche en mathématiques: énoncé du
  théorème, exemples, hypothèse de récurrence, reste de la preuve.

- Dans l'exemple ci-dessus, les invariants étaient écrits dans des
  commentaires. Lisibles par l'homme, donc, mais inexploitable par la
  machine. Chaque fois que possible, exprimez vos invariants sous une
  forme *exécutable* tout en restant *lisible*. Cela se fait
  typiquement avec:

      assert ...
    
  Dans la phase de mise au point, cette forme permet de vérifier
  systématiquement les invariants, et d'arêter l'exécution du
  programme le plus tôt possible en cas de problème. Lors de la mise
  en production, il est possible de désactiver la vérification des
  asserts (option -O en Python) pour ne pas pénaliser la vitesse
  d'exécution.
:::

Vous êtes maintenant prêts à aborder les [parcours en
largeur](02-ParcoursEnLargeur.md).

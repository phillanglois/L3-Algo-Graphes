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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "d41bfa52589cd39d02b7cce6e404d2fb", "grade": false, "grade_id": "cell-28d494e048f3ca33", "locked": true, "schema_version": 3, "solution": false, "task": false}}

# Plus courts chemins, avec poids: l'[algorithme de Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra)

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "cd74ce19e73fe11ae10dfcdb86562b29", "grade": false, "grade_id": "cell-2418dd5b544980bf", "locked": true, "schema_version": 3, "solution": false, "task": false}}

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
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 1ac169d9a7aebcf9639855cc71633e66
  grade: false
  grade_id: cell-932285cf25ec6af1
  locked: true
  schema_version: 3
  solution: false
  task: false
---
G = examples.dijkstra()
G.show()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "32c631358c34369d5626ccf66282b856", "grade": false, "grade_id": "cell-541e8093bec607c5", "locked": true, "schema_version": 3, "solution": false, "task": false}}

On souhaite calculer le plus court chemin entre deux sommets de ce graphe.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "f72f5be669bb451b271089dc4b90110c", "grade": false, "grade_id": "cell-9052d311cb4ac13d", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice

1.  Complétez la fonction `dijkstra` du fichier [dijkstra.py](dijkstra.py).
2.  Appliquez cette fonction au graphe `G` ci-dessus:

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 2e0bca3fd9fc01af654994bedd305fc9
  grade: false
  grade_id: cell-f52c1bf66d323bc2
  locked: false
  schema_version: 3
  solution: true
  task: false
---
# VOTRE CODE ICI
raise NotImplementedError()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "497d88dd6ebd07a3a2552d5026f29a64", "grade": false, "grade_id": "cell-09260c8bcd80db6a", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice, suite

3.  Déduisez en la distance entre `A` et `J`, à mettre dans la
    variable `distance_AJ`:

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: c4b4ca3e455fd152e6b71f55744fd3b5
  grade: false
  grade_id: cell-1f02da44eb448e2d
  locked: false
  schema_version: 3
  solution: true
  task: false
---
# VOTRE CODE ICI
raise NotImplementedError()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 3b2f53ed51085364bdc399158c67e0bc
  grade: true
  grade_id: cell-4efcd06723aa15a5
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
# Vérifie votre résultat sans dévoiler la solution, par la magie des fonctions de hachage :-)
import hashlib
assert hashlib.md5(bytes(distance_AJ)).hexdigest() == '2f6064003b888e403627e493532fc751'
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: a584f2035c87031e18955205fab9281a
  grade: true
  grade_id: cell-0d543769776d9f6a
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
distances = dijkstra(G, "A")[0]
assert distances["A"] == 0
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 88aae391bdb7b04d2c9f89d7abc22bcf
  grade: true
  grade_id: cell-4670834a66e9e247
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert sum(distances.values()) == 2774
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ac1e3724b20c941f074bb2a8cc9ed0e5", "grade": false, "grade_id": "cell-73fa8b07519bc08b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice, suite

4.  Implantez la fonction `shortest_path` dans [dijkstra.py](dijkstra.py), et utilisez là pour calculer un plus court chemin entre `A` et `J` dans `G`:

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 7707819c72c8f3d542e9132401d38233
  grade: true
  grade_id: cell-6e6fadae5c937751
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
# VOTRE CODE ICI
raise NotImplementedError()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "476c05008956170051462645c089493c", "grade": false, "grade_id": "cell-bc2add573b4d29c0", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice, suite

5.  Pour aller plus loin : Instrumentez votre fonction pour en visualiser l'exécution.

:::

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "86a02fb714ac8def08489b6631b6758d", "grade": false, "grade_id": "cell-c329346b38dade70", "locked": true, "schema_version": 3, "solution": false, "task": false}}

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
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 2d8a4e2bd28567f979b6abeb6d3f54fc
  grade: false
  grade_id: cell-fb08b16fd3f410f4
  locked: false
  schema_version: 3
  solution: true
  task: false
---
# VOTRE CODE ICI
raise NotImplementedError()
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 66292b6efd0341ac217b0f9508244616
  grade: false
  grade_id: cell-739afeadecf4cfae
  locked: false
  schema_version: 3
  solution: true
  task: false
---
# VOTRE CODE ICI
raise NotImplementedError()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: f71fc4b187d4c3e9c881ecbfccde1ff9
  grade: true
  grade_id: cell-9e4d0bcecc9cb8ab
  locked: true
  points: 3
  schema_version: 3
  solution: false
  task: false
---
# Vérifie votre résultat sans dévoiler la solution, par la magie des fonctions de hachage :-)
import hashlib
assert hashlib.md5(bytes(int(distance))).hexdigest() == '47699f4b69b37670eb6ce45276ad9a30'
```

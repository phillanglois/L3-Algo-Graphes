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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "e46576ecb897d30a7b55a0aa13228702", "grade": false, "grade_id": "cell-115fa66af785d4a2", "locked": true, "schema_version": 3, "solution": false, "task": false}}

# Parcours en profondeur

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "e9fb590c3a6fb44d899759e70f92ef5f", "grade": false, "grade_id": "cell-916f6e1be3f587ad", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice

1.  Implantez l'algorithme de parcours en profondeur par une fonction
    récursive comme décrite sur la page
    [Wikipedia](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur).

:::

```{code-cell} ipython3
from graph import Graph, Node, examples
from typing import List
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 6aa1af4fa565e798758634a229b395a9
  grade: false
  grade_id: cell-51be940219a4d59a
  locked: false
  schema_version: 3
  solution: true
  task: false
---
def parcours_en_profondeur_recursif(G: Graph, u: Node) -> List[Node]:
    """
    INPUT:
    - 'G' - un graphe
    - 'u' - un sommet du graphe
    
    OUTPUT: La liste des sommets obtenus par un parcours en profondeur
    de `G` à partir de `u`.

    """
    # VOTRE CODE ICI
    raise NotImplementedError()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "03d461433e7fce07259947edb83a5fbf", "grade": false, "grade_id": "cell-916f6e1be3f587ae", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice, suite

2.  Vérifiez votre implantation à l'aide des tests suivants:

:::

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 6dc088dcecac485d3f44be00dbe1e0bd
  grade: false
  grade_id: cell-d1ed6ac7ee3f79a3
  locked: true
  schema_version: 3
  solution: false
  task: false
---
import unittest
# Tests inspirés de:
# - https://sahandsaba.com/review-of-basic-algorithms-and-data-structures-in-python-graph-algorithms.html#depth-first-search-dfs
# - https://codereview.stackexchange.com/questions/153225/dfs-algorithm-unit-test
class DFSTest(unittest.TestCase):
    def test_single_vertex(self):
      graph = Graph([0])
      self.assertEqual(dfs(graph, 0), [0])
    
    def test_single_vertex_with_loop(self):
      graph = Graph([0], edges=[(0, 0, 1)])
      self.assertEqual(dfs(graph, 0), [0])
    
    def test_two_vertices_no_path(self):
      graph = Graph([0,1])
      self.assertEqual(dfs(graph, 0), [0])
      self.assertEqual(dfs(graph, 1), [1])
    
    def test_two_vertices_with_simple_path(self):
      graph = Graph([0,1], edges=[(0,1,1)], directed=True)
      self.assertEqual(dfs(graph, 0), [0, 1])
      self.assertEqual(dfs(graph, 1), [1])
    
    def test_complete_graph(self):
      for n in range(2, 10):
        graph = examples.complet(n)
        for v in range(n):
          self.assertEqual(set(dfs(graph, v)),  set(range(n)))
    
    def test_cycle_5(self):
        n = 5
        graph = examples.C5()
        for v in range(n):
            self.assertEqual(dfs(graph, v), list(range(v,n)) + list(range(0,v)))

    def test_(self):
        graph = Graph(["A", "B", "C", "D", "E", "F"],
                      edges=[("A", "B", 1), ("B", "C", 1), ("C", "D", 1),
                             ("A", "E", 1), ("E", "F", 1), ("F", "D", 1)],
                      directed=True
                     )
        self.assertEqual(dfs(graph, "A"), ["A", "B", "C", "D", "E", "F"])
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: b853198c2cb00fbbff04e83308584e39
  grade: true
  grade_id: cell-29270b388637a30d
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
dfs = parcours_en_profondeur_recursif
result = unittest.main(argv=[''], verbosity=0, exit=False).result
assert result.failures, "Tous les tests ne sont pas passés"
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "3ff81e16ff1361dcf55667978c580252", "grade": false, "grade_id": "cell-e3a78a0dac24e12a", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice, suite

3.  Reprenez l'algorithme de la feuille
    [01-ParcoursDeGraphe.md](01-ParcoursDeGraphe.md) en utilisant une
    pile à la place d'une file pour `todo`.

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: aa52a24c923cf2ab6c01314bcd160c1b
  grade: false
  grade_id: cell-cabfa71f42e78d26
  locked: false
  schema_version: 3
  solution: true
  task: false
---
def parcours_en_profondeur(G: Graph, u: Node) -> List[Node]:
    """
    INPUT:
    - 'G' - un graphe
    - 'u' - un sommet du graphe
    
    OUTPUT: un parcours en profondeur de `G`
    """
    # VOTRE CODE ICI
    raise NotImplementedError()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "5dbc2c466d65d20b374954035d342a0c", "grade": false, "grade_id": "cell-3c315233b823c828", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Tests:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 28e176b8537474d7610ecfbbdf12268f
  grade: true
  grade_id: cell-4179a581ce7b7973
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
dfs = parcours_en_profondeur
result = unittest.main(argv=[''], verbosity=0, exit=False).result
assert not result.failures, "Tous les tests ne sont pas passés"
```

```{code-cell} ipython3

```

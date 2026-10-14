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

# Bibliothèque de graphes

Vous retrouverez dans <a href="graph.py">graph.py</a> le squelette de la classe
`Graph` que vous avez implanté la séance dernière. Remplacez-le par
votre implantation, puis vérifiez que tout fonctionne:

```{code-cell} ipython3
:deletable: false
:editable: false

from graph import Graph, examples
```

```{code-cell} ipython3
---
nbggrader:
  grade: true
  grade_id: cell-1dd035627b5d7b54
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
G = Graph([1,2,3], edges=[(1,2,"12"),(2,3,"23")])
```

```{code-cell} ipython3
:deletable: false
:editable: false

assert sorted(G.edges()) == sorted(((1, 2, '12'), (2, 1, '12'), (2, 3, '23'), (3, 2, '23')))
```

```{code-cell} ipython3
:deletable: false
:editable: false

G.show()
```

```{code-cell} ipython3
:deletable: false
:editable: false

G = examples.cours_1_G()
G.edges()
```

```{code-cell} ipython3
:deletable: false
:editable: false

assert G.number_of_nodes() == 6
```

+++ {"deletable": false, "editable": false}

Maintenant, lancez tous les tests inclus dans la documentation des fonctions:

```{code-cell} ipython3
:deletable: false
:editable: false

from utils import code_checker
code_checker("pytest graph.py")
```

```{code-cell} ipython3
:deletable: false
:editable: false

code_checker("ruff check --ignore E741 graph.py")
```

```{code-cell} ipython3
:deletable: false
:editable: false

code_checker("mypy graph.py")
```

+++ {"deletable": false, "editable": false}

Évaluation de l'implantation des méthodes et de la complexité

```{code-cell} ipython3
:deletable: false
:editable: false

from utils import show_source
show_source(Graph.successors)
show_source(Graph.predecessors)
show_source(Graph.capacity)
show_source(Graph.is_path)
```

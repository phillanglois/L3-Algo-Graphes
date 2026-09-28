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

+++ {"deletable": false, "editable": false, "grade_id": "cell-1d836c2f9268f0e1", "tags": ["locked"]}

# Rapport de TP

+++ {"deletable": false, "grade_id": "cell-892ec4c17e615b9b", "points": 0, "tags": ["answer"]}

Cellule cell-892ec4c17e615b9b

% REMPLACEZ CETTE LIGNE PAR VOTRE RÉPONSE

+++ {"deletable": false, "editable": false, "grade_id": "cell-f00c118da0fb33b6", "points": 0, "tags": ["locked"]}

## Qualité du code

+++

Liste des fichiers de code :

- [graph.py](graph.py)
- ...

+++ {"deletable": false, "editable": false, "grade_id": "cell-5d42db0fdaf62572", "tags": ["locked"]}

Vérification de syntaxe et de style :

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-e5e7a8b97e5fb0fe
:points: 1
:tags: [test]
:test: true

from utils import code_checker
code_checker("ruff check --ignore E741 --exclude nbgrader_config.py")
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-c45ae33a6e876c00", "tags": ["locked"]}

Vérification statique de types :

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-c9f65f41df4f145b
:points: 1
:tags: [test]
:test: true

code_checker("mypy .")
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-dc7cfd25d520b9d7", "tags": ["locked"]}

Tests unitaires :

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-6fb4d07f94265690
:points: 4
:tags: [test]
:test: true

code_checker("pytest --junit-xml=feedback/pytest.xml")
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-e24ca78e8b1b2c8b", "tags": ["locked"]}

## Code et complexité

Cette section sera plus développée dans le TP suivant.

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-1c9b3a5e0d64360c
:tags: [locked]

from graph import Graph
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-69687d1f6ff2d2cf", "points": 0, "tags": ["locked"]}

Code et complexité de `number_of_edges` :

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-7f9eaeca83d5712d
:tags: [locked]

from utils import show_source
show_source(Graph.number_of_edges)
```

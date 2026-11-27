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

+++ {"nbgrader": {"schema_version": 3, "solution": false, "grade": false, "locked": true, "task": false, "grade_id": "cell-3a7df4315a12405c"}}

# Thème 4: arbres couvrants

+++

Effectuez les feuilles suivantes dans l'ordre, en cochant au fur et à
mesure celles que vous aurez faites :

- [ ] [](1-Cycles.md)
- [ ] [](2-ArbresCouvrants.md)
- [ ] [](3-Kruskal.md)
- [ ] [](4-UnionFind.md)

+++

## Mini rapport de TP

+++ {"nbgrader": {"grade": true, "grade_id": "cell-892ec4c17e615b9b", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}}

### En quelques mots, qu'avez-vous appris?

BEGIN SOLUTION
END SOLUTION

### Quelles difficultés avez vous éventuellement rencontrées?

BEGIN SOLUTION
END SOLUTION

### Qu'avez vous aimé ou moins aimé dans ce TP?

BEGIN SOLUTION
END SOLUTION

### Notes et commentaires libres

+++ {"nbgrader": {"schema_version": 3, "solution": false, "grade": false, "locked": true, "task": false, "grade_id": "cell-f00c118da0fb33b6"}}

## Qualité du code

+++ {"nbgrader": {"schema_version": 3, "solution": false, "grade": false, "locked": true, "task": false, "grade_id": "cell-5d42db0fdaf62572"}}

Vérification de syntaxe et de style:

```{code-cell} ipython3
---
nbgrader:
  grade: true
  grade_id: cell-e5e7a8b97e5fb0fe
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
from utils import code_checker
code_checker("ruff check --ignore E741 --exclude nbgrader_config.py")
```

+++ {"nbgrader": {"schema_version": 3, "solution": false, "grade": false, "locked": true, "task": false, "grade_id": "cell-c45ae33a6e876c00"}}

Vérification statique de types:

```{code-cell} ipython3
---
nbgrader:
  grade: true
  grade_id: cell-c9f65f41df4f145b
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
code_checker("mypy .")
```

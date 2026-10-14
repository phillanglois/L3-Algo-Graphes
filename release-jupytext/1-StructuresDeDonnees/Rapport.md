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

+++ {"deletable": false, "editable": false}

# Rapport de TP

+++ {"deletable": false}

L'objectif du rapport de TP est de donner une synthèse du travail réalisé. Pour cette
séance, cette synthèse peut-être réalisée quasi automatiquement avec les outils de
vérification de code combinés avec ce que vous avez déjà rédigé dans la documentation des
méthodes. Vous n'avez donc que quelques mots à écrire ci-dessous.

## En quelques mots, qu'avez-vous appris?

% REPLACE THIS LINE BY YOUR ANSWER

## Quelles difficultés avez vous éventuellement rencontrées?

% REPLACE THIS LINE BY YOUR ANSWER

## Qu'avez vous aimé ou moins aimé dans ce TP?

% REPLACE THIS LINE BY YOUR ANSWER

## Notes et commentaires libres

+++ {"deletable": false, "editable": false}

## Qualité du code

+++

Liste des fichiers de code :

- [graph.py](graph.py)
- ...

+++ {"deletable": false, "editable": false}

Vérification de syntaxe et de style :

```{code-cell} ipython3
:deletable: false
:editable: false

from utils import code_checker
```

```{code-cell} ipython3
:deletable: false
:editable: false

code_checker("ruff check --ignore E741 --exclude nbgrader_config.py")
```

+++ {"deletable": false, "editable": false}

Vérification statique de types :

```{code-cell} ipython3
:deletable: false
:editable: false

code_checker("mypy .")
```

+++ {"deletable": false, "editable": false}

Tests unitaires :

```{code-cell} ipython3
:deletable: false
:editable: false

code_checker("pytest -v --junit-xml=feedback/pytest.xml")
```

+++ {"deletable": false, "editable": false}

## Code et complexité

Cette section sera plus développée dans le TP suivant.

```{code-cell} ipython3
:deletable: false
:editable: false

from graph import Graph
```

+++ {"deletable": false, "editable": false}

Code et complexité de `number_of_edges` :

```{code-cell} ipython3
:deletable: false
:editable: false

from utils import show_source
show_source(Graph.number_of_edges)
```

```{code-cell} ipython3

```

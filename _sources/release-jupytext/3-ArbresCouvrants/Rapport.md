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

# Mini rapport de TP

+++ {"deletable": false}

## En quelques mots, qu'avez-vous appris?

% REPLACE THIS LINE BY YOUR ANSWER

## Quelles difficultés avez vous éventuellement rencontrées?

% REPLACE THIS LINE BY YOUR ANSWER

## Qu'avez vous aimé ou moins aimé dans ce TP?

% REPLACE THIS LINE BY YOUR ANSWER

## Notes et commentaires libres

+++ {"deletable": false, "editable": false}

## Qualité du code

+++ {"deletable": false, "editable": false}

Vérification de syntaxe et de style:

```{code-cell} ipython3
:deletable: false
:editable: false

from utils import code_checker
code_checker("ruff check --ignore E741 --exclude nbgrader_config.py")
```

+++ {"deletable": false, "editable": false}

Vérification statique de types:

```{code-cell} ipython3
:deletable: false
:editable: false

code_checker("mypy .")
```

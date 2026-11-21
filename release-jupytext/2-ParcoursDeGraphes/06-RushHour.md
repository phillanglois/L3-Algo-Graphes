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

# Problème 2: [Rush Hour](http://www.thinkfun.com/products/rush-hour/)


La voiture rouge est coincée dans un embouteillage; comment déplacer les véhicules pour la faire sortir?
Ci-dessous le défi 1 :
<center>

:::{image} media/rush_hour.gif
:width: "30%"
:alt: Une image du jeu Rush Hour
:::

</center>

+++ {"deletable": false, "editable": false}

Quel rapport avec les parcours de graphes? Saurez-vous faire résoudre par l'ordinateur le défi 40 en un nombre minimum du coups?

+++ {"deletable": false, "editable": false}

Dans cette feuille, vous découvrirez le modèle et deux mini applications interactives pour le jeu RushHour qui vous sont fournis. Il ne restera «plus qu'à» implanter l'«Intelligence Artificielle» pour résoudre le jeu.

+++ {"deletable": false, "editable": false}

## Un modèle pour RushHour

+++

##  Le jeu RushHour

Voici une [présentation et les règles](rushhour.md) de ce jeu.

+++ {"deletable": false, "editable": false}

### Quelques exemples d'utilisation de [rush_hour.py]()

```{code-cell} ipython3
:deletable: false
:editable: false

from rush_hour import Plateau
```

```{code-cell} ipython3
plateau = Plateau(['A2R00','X2R21','C2R44','R3R52','O3D05','P3D10','Q3D13','B2D40']); plateau
```

```{code-cell} ipython3
plateau.recule("Q")
```

```{code-cell} ipython3
plateau.est_gagnant()
```

+++ {"deletable": false, "editable": false}

Chargement du 40ème défi de RushHour (voir les fichiers dans [RushHourDefis/](RushHourDefis/)) :

```{code-cell} ipython3
Plateau(40)
```

+++ {"deletable": false, "editable": false}

### Un exemple d'interface utilisateur minimale

```{code-cell} ipython3
:deletable: false
:editable: false

from ipywidgets import interact_manual
from rush_hour import Plateau
plateau = Plateau(['A2R00','X2R21','C2R44','R3R52','O3D05','P3D10','Q3D13','B2D40']); plateau
@interact_manual
def step(voiture=plateau.voitures.keys(), distance=[0,-1,1]):
    global plateau
    plateau2 = plateau.avance(voiture, distance)
    if plateau2:
        plateau = plateau2
    return plateau
```

+++ {"deletable": false, "editable": false}

## Une application graphique basée sur les widgets de Jupyter

```{code-cell} ipython3
:deletable: false
:editable: false

from rush_hour_application import RushHourApplication
A = RushHourApplication()
A
```

+++ {"deletable": false, "editable": false}

## À vous de jouer !

+++ {"deletable": false, "editable": false}

Implantez la méthode `solution` dans la classe [RushHour](rush_hour.py) pour déterminer une séquence minimale de coup permettant de résoudre un défi, puis utilisez la ci-dessous pour résoudre le défi 40 de Rush Hour.

+++ {"deletable": false, "editable": false}

:::{admonition} Indications
:class: hint dropdown
- Considérez le graphe dont les sommets sont les états possibles du plateau et les arêtes les déplacements de voiture !
- Analyser les classes/objets `Voiture` et `Plateau` définies dans `rush_hour.py`. par exemple :
    - comment est représentée la position d'une voiture ?
    - quelle(s) représentation(s) du plateau ? 
    - comment vérifier que le plateau est dans un état "gagnant" ?
:::

```{code-cell} ipython3
:deletable: false
:editable: false

from rush_hour import RushHour
solution = RushHour.solution(40, verbeux = True)
```

```{code-cell} ipython3
:deletable: false
:editable: false

assert RushHour.est_solution(40, solution)
```

+++ {"deletable": false, "editable": false}

**Optionnel.**

Les étapes suivantes pour évaluer la qualité du code.

```{code-cell} ipython3
:deletable: false
:editable: false

from utils import show_source
show_source(RushHour.solution)
```

```{code-cell} ipython3
:deletable: false
:editable: false

from utils import code_checker, show_source
code_checker("ruff check rush_hour.py")
```

```{code-cell} ipython3
code_checker("mypy rush_hour.py")
```

```{code-cell} ipython3
:deletable: false
:editable: false

code_checker("pytest rush_hour.py")
```

```{code-cell} ipython3

```

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

+++ {"deletable": false, "editable": false, "grade_id": "cell-340372ef6a82d730", "tags": ["locked"]}

# Prise en main de l'environnement de travail

+++ {"deletable": false, "editable": false, "grade_id": "cell-340372ef6a82d731", "tags": ["locked"]}

Suivez les
[instructions](http://nicolas.thiery.name/Enseignement/M1-ISD-AlgorithmiqueAvancee/ComputerLab/README.html#telechargement-et-depot-des-tps)
pour accéder à l'environnement de travail et téléchargez le TP.

Puis ouvrez cette première feuille Jupyter `00-PriseEnMain`.

+++ {"deletable": false, "editable": false, "grade_id": "cell-340372ef6a82d732", "tags": ["locked"]}

## Prise en main de Jupyter

+++ {"deletable": false, "editable": false, "grade_id": "cell-340372ef6a82d733", "tags": ["locked"]}

Cette feuille est dédiée à la prise en main des feuilles de travail Jupyter (que la
plupart d'entre vous connaisse), ainsi que du mécanisme de correction semi-automatique
que nous utiliserons dans ce cours.

+++ {"deletable": false, "editable": false, "grade_id": "cell-4911a792a82448d7", "tags": ["locked"]}

Une analyse de données prend la forme d'un document narratif expliquant les objectifs,
hypothèses et étapes de l'analyse: quelles sont les données, qu'est-ce que l'on souhaite
calculer, pourquoi, comment, quels sont les résultats et quelles conclusions on en tire.
Ce document est typiquement écrit en anglais pour qu'il puisse être partagé avec le plus
grand nombre.

+++ {"deletable": false, "editable": false, "grade_id": "cell-49874ed5d0338eec", "tags": ["locked"]}

Depuis quelques années, les feuilles de travail (notebook) Jupyter sont un des moyens
prisés pour rédiger de telles analyses de données et mener les calculs sous-jacents. Il
s'agit en effet de documents permettant de mêler narration, interaction, calcul,
visualisation et programmation.

+++ {"deletable": false, "editable": false, "grade_id": "cell-49874ed5d0338eed", "tags": ["locked"]}

Le document que vous êtes en train de lire est une feuille Jupyter. On peut y mettre des
calculs comme ci-dessous. Pour exécuter le calcul, cliquez dans la *cellule* ci-dessous
et tapez Shift-Enter:

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-02a086c93b3ab3f2
:tags: [locked]

1 + 1
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-aa712b4c2a825a98", "tags": ["locked"]}

Utilisez maintenant la cellule ci-dessous pour calculer 1+2; puis réutilisez la même
cellule pour calculer 3×4:

```{code-cell} ipython3

```

+++ {"deletable": false, "editable": false, "grade_id": "cell-20435b0654662bc4", "tags": ["locked"]}

Vous rencontrerez aussi des cellules à compléter comme la suivante dans lesquelles vous
remplacerez la ligne «# Remplacez cette ligne par votre code» par le calcul à faire.
Calculez cinq fois sept:

```{code-cell} ipython3
:deletable: false
:grade_id: cell-d8b61dce71965f3e
:points: 0
:tags: [answer]

# Cellule cell-d8b61dce71965f3e
# REMPLACEZ TOUTE CETTE LIGNE PAR VOTRE CODE
```

+++ {"deletable": false, "grade_id": "cell-b35d0d71e7e10dd3", "points": 1, "tags": ["answer"]}

Cellule cell-b35d0d71e7e10dd3

Vous pouvez aussi éditer les cellules contenant du texte comme celle-ci. Allez-y:
double-cliquez dans la cellule, présentez vous en la complétant, puis appuyez sur
Shift-Enter.

- Nom:

  % REMPLACEZ CETTE LIGNE PAR VOTRE RÉPONSE

- Prénom:

  % REMPLACEZ CETTE LIGNE PAR VOTRE RÉPONSE

- Quelques mots sur votre expérience passée avec Python:

  % REMPLACEZ CETTE LIGNE PAR VOTRE RÉPONSE

- avec Jupyter:

  % REMPLACEZ CETTE LIGNE PAR VOTRE RÉPONSE

- avec git:

  % REMPLACEZ CETTE LIGNE PAR VOTRE RÉPONSE

- avec la théorie des graphes:

  % REMPLACEZ CETTE LIGNE PAR VOTRE RÉPONSE

- Commentaires libres:

  % REMPLACEZ CETTE LIGNE PAR VOTRE RÉPONSE

+++ {"deletable": false, "editable": false, "grade_id": "cell-20435b0654662bc2", "tags": ["locked"]}

On peut ausi mettre des formules mathématiques dans une cellule:
$$\frac 1 {1-\frac 1z} = \sum_{i=0}^\infty \frac 1 {z^i}$$

+++ {"deletable": false, "editable": false, "grade_id": "cell-20435b0654662bc5", "tags": ["locked"]}

Notez que certaines cellules de ce document comme celle-ci sont en lecture-seule. Vous ne
pouvez pas les modifier. En revanche, vous pouvez toujours insérer de nouvelles cellules.

Insérez une nouvelle cellule ci-dessous, et mettez y la formule $E=mc^2$:

Indications:

- Boutton + de la barre de menu de la feuille
- sélectionnez la cellule
- changez son type en `MarkDown` (voir la barre de menu de la feuille)
- double-cliquez sur cette cellule ou la précédente pour voir comment insérer des
  formules mathématiques en latex.

+++ {"deletable": false, "editable": false, "grade_id": "cell-20435b0654662bc6", "tags": ["locked"]}

- Lancez la visite guidée de l'interface Jupyter.<br> Indication: Menu `Aide` ->
  `Visite de l'interface utilisateur`.
- Consultez les raccourcis claviers.<br> Indication: Menu `Aide` -> `Raccourcis clavier`.

+++ {"deletable": false, "editable": false, "grade_id": "cell-20435b0654662bc7", "tags": ["locked"]}

## Correction semi-automatique avec nbgrader

+++ {"deletable": false, "editable": false, "grade_id": "cell-20435b0654662bc8", "tags": ["locked"]}

Certaines feuilles de travail seront notées. Les notes de certaines séances ultérieures
contribueront à votre moyenne. Cette première séance est une séance d'entraînement; les
notes seront indicatives pour que vous preniez en main le mécanisme.

Une partie de la correction est manuelle: vos enseignants regarderont vos réponses et
attribueront des points à chacune d'entre elles. Le gros de la correction sera
automatique, s'appuyant sur des tests similaires à ceux du premier semestre.

Voici un exemple tout bête. Dans la cellule suivante, calculez la somme de `3` et de `4`,
et stockez le résultat dans la variable `s`:

```{code-cell} ipython3
:deletable: false
:grade_id: cell-d8b61dce71965f3g
:tags: [answer]

# Cellule cell-d8b61dce71965f3g
# REMPLACEZ TOUTE CETTE LIGNE PAR VOTRE CODE
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-074eb18a150a2c8e", "tags": ["locked"]}

La commande suivante est un test qui vérifie votre réponse; vous reconnaîtrez le `assert`
(cette fois en minuscule) que nous utilisions en C++ au premier semestre:

```{code-cell} ipython3
:deletable: false
:editable: false
:grade_id: cell-d8b61dce71965f3h
:points: 1
:tags: [test]
:test: true

assert s == 7
```

+++ {"deletable": false, "editable": false, "grade_id": "cell-4c9512739b1f0f29", "tags": ["locked"]}

<!--Validez votre feuille en cliquant sur le bouton `Validate`; cela en
exécute une copie dans l'ordre en vérifiant tous les tests
automatiques.!-->

Suivez les
[instructions](http://nicolas.thiery.name/Enseignement/M1-ISD-AlgorithmiqueAvancee/ComputerLab/README.html#telechargement-et-depot-des-tps)
pour déposer votre travail sur GitLab et obtenir les résultats de la correction
automatique.

:::{important}

Les résultats de la correction automatique sont indicatifs. Mais ce que vous allez
développer servira dans tous les TPs suivants. Vous devez viser un zéro faute :-) En
sus, la qualité du code de ce TP et de sa documentation sera l'un des éléments de la
notation du TP 2.
:::

+++ {"deletable": false, "editable": false, "grade_id": "cell-3d7e1f615bba7ace", "tags": ["locked"]}

:::{admonition} Apprenez à utiliser Jupyter comme un pro!
:class: important

Il sera essentiel, pour ce cours et pour la suite, de devenir un utilisateur expert de
Jupyter, notamment en ce qui concerne l'utilisation des raccourcis. Pour cela, vous avez
par exemple à votre disposition ce
[tutoriel](https://tutoriels-jupyter.pages.in2p3.fr/lite/lab?path=tutoriel/index.ipynb),
à faire hors séance.
:::

+++ {"deletable": false, "editable": false, "grade_id": "cell-8226871d2f13ccb8", "tags": ["locked"]}

## Au boulot!

Maintenant que vous avez appris les rudiments de Jupyter et de l'environnement de
travail; il est temps de passer au [TP](01-Introduction.md) lui-même!

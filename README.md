---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: pandoc
      format_version: 3.1.11
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  nbformat: 4
  nbformat_minor: 5
---

::: {#15210705-13da-4716-b35c-3e62ddc5ba13 .cell .markdown}
# Algorithmique des graphes

Ce dépôt à destination des L3 Informatique et Mathématiques de l'UPVD reprend le cours

**Algorithmique avancée** du

M1 Informatique pour la Science des Données, Université Paris-Saclay, Faculté d'Orsay

[Page web](http://nicolas.thiery.name/Enseignement/M1-ISD-AlgorithmiqueAvancee/),
[ENT eCampus](https://ecampus.paris-saclay.fr/course/view.php?name=UPSAY_2025_940_UE_O4INA12)

-   Les passages modifiés par rapport à l\'original sont précédés du tag #UPVD.
-   Certains passages spécifiques à l\'[organisation parisienne](http://nicolas.thiery.name/Enseignement/M1-ISD-AlgorithmiqueAvancee) on été supprimés.

+++

«L'objectif de ce cours est de fournir des outils et techniques
algorithmiques de pointe aux apprentis. Étude de l'algorithmique sur
les graphes (plus courts chemins, tri topologique, ...), les techniques de
mémorisation, de programmation dynamique et de backtracking.
Présentation de la notion de flots et des algorithmes de calcul de flot
maximal. Enfin, les thèmes des algorithmes online et approchés seront
abordés.»

+++

## Enseignants à l\'origine de ces supports

-   [Florent Hivert](https://www.lri.fr/~hivert/) (pas cette année)
-   [Viviane Pons](https://www.lri.fr/~pons/en/) (pas cette année)
-   [Nicolas M. Thiéry](http://Nicolas.Thiery.name)

### #UPVD Enseignant pour cette expérimentation à l'UPVD

-   [Philippe Langlois](http://perso.univ-perp.fr/langlois)
:::

::: {#0b832a15-b79a-4809-bfe9-33c8574861aa .cell .markdown}
+++

## Vue d'ensemble

+++

Les notions du cours seront abordées par la pratique, tout d'abord par
l'implantation de structures de données de graphes, puis leur
utilisation pour résoudre quatre problèmes.

+++

### Structures de données pour les graphes

+++

### Problème 1 : Le chemin le plus rapide en métro de Montgallet à Billancourt ? {#problème-1--le-chemin-le-plus-rapide-en-métro-de-montgallet-à-billancourt-}

:::{figure} media/metro-paris.gif
:width: 50%
:::

::: {#56aca199-da03-4780-8561-0e7e24739828 .cell .markdown}
+++

### Problème 2 : [Rush Hour](http://www.thinkfun.com/products/rush-hour/) {#problème-2--rush-hour}

La voiture rouge est coincée dans un embouteillage; comment déplacer les véhicules pour la faire sortir?
Ci-dessous le défi 1. Saurez-vous faire résoudre par l'ordinateur le défi 40 en un nombre minimum du coups?

:::{figure} media/rush_hour.gif
:alt: Un visuel du jeu de plateau RushHour
:::

::: {#5025a5fa-6292-45a2-b60c-bd048d51939d .cell .markdown}
+++

### Problème 3 : Faire passer le maximum de courant {#problème-3--faire-passer-le-maximum-de-courant}

:::{figure} media/reseau-electrique.png
:width: 50%
:::

::: {#ab5e0dd0-09ed-4306-ab70-93fd544e8083 .cell .markdown}
+++

### Problème 4 : Fabriquer et résoudre des labyrinthes {#problème-4--fabriquer-et-résoudre-des-labyrinthes}

:::{figure} media/labyrinthe.png
:width: 50%

+++
:::

::: {#39dfdfba-86a2-4ecd-9cc8-86d38eb30e39 .cell .markdown}
## #UPVD Planning

+++

12 séances de 3h: Cours ou cours + TD + TP intégré

mercredi 14h-17h, salle banalisée (1h30) puis salle info (1h30)

+++

### Graphes: structures de données, terminologie, plus courts chemins

-   2026-09-09
    2026-09-16 (+ test Python)

+++

### Arbres couvrants

+++

### Parcours et plus court chemin

+++

### Réseaux et flots

+++

### CC et CT

Semaine des examens

+++

## #UPVD Modalités d'évaluation

L'évaluation se fera sur vos TPs, évalués à l'oral (CC), ainsi que sur un examen (CT)

Note UE : 1/2 CC + 1/2 CT

+++

### Annales

Désolé, je n'en n'ai pas encore.

+++

## Du bon usage des aides

Vous avez à disposition de multiples aides: enseignant, solutions en
ligne, collègues, copains, famille, robots conversationnels, etc.

**Vous êtes responsables de votre progression, à vous de les utiliser
à bon escient.**

+++

:::{admonition} Nos conseils
:class: tip

-   Les exercices de ce cours sont à réaliser par vous-même pour qu'ils
    soient utiles à votre progression. Copier ou simplement adapter une
    solution existante ne vous apportera pas grand chose.
-   Si, après un temps de réflexion personnelle approfondie, vous ne
    voyez pas comment avancer, alors n'hésitez pas à demander **des
    indications** à vos aides.\
    Si vous vous adressez à un robot conversationnel, soyez précis dans
    votre invite (prompt): «Vous êtes un enseignant bienveillant d'un
    cours de master d'algorithmique de graphes. Je dois résoudre
    l'exercice suivant: ... J'ai essayé ... Sans me donner la solution,
    pourriez vous me donner une indication sur comment avancer à partir
    de là?»
-   Vous pouvez aussi utiliser vos aides pour discuter vos solutions aux
    exercices.
-   Privilégiez les conversations avec des humains; elles sont plus
    fécondes qu'avec un robot.\
    **Vous êtes aussi responsable de votre impact environnemental**
:::

::: {#ba99d7dd-2e17-4a3d-bc82-dbd63cd22b3e .cell .markdown}
+++

:::{admonition} Évaluation des TPs
:class: hint

Vous ne serez pas évalués sur vos rendus de TP, mais lors de deux ou
trois mini-oraux portant sur le thème des TPs.

Motivation:

-   Vous inciter à **comprendre** les TPs plus qu'à les **remplir**.
-   Consacrer mon temps de correction des TPs à des dialogues individuel
    féconds, plutôt qu'à faire le flic et compter des points derrière
    mon ordi.
-   Vous faire remémorer vos TPs après la fin de ceux-ci, pour aider à
    ancrer les apprentissages sur le plus long terme.
:::

::: {#9249e815-d01b-4a8d-b954-fd6848db4d44 .cell .markdown}
+++

## Environnement de travail

-   Langage de programmation: Python 3
-   Bibliothèques: networkx + matplotlib + ...
-   Environnement interactif: [Jupyter](https://jupyter.org)
-   Forge logicielle: GitHub

+++

Dans cette section, nous expliquons:

-   Comment accéder aux logiciels requis
-   Comment télécharger et déposer vos devoirs

Les instructions font l'hypothèse que vous travaillerez sur ce cours dans votre
répertoire `~/L3-AlgoGraphes`. Vous pouvez choisir un autre nom.

+++

### Accéder aux logiciels requis

Ce cours utilise Python, Jupyter et quelques bibliothèques classiques (voir le
fichier [pyproject.toml](pyproject.toml), ainsi que quelques paquets Python plus ou
moins maison.

::::{admonition} #UPVD Installation en local de l'environnement de travail

Vous devez installer les logiciels sur votre machine et travailler en
local.

::::{admonition} #UPVD Instructions d'installation avec `uv`

1.  Si vous ne l'avez pas déjà fait, installez le gestionnaire d'environnements
    [uv](https://docs.astral.sh/uv/getting-started/installation/).

2.  Si vous ne l'avez pas déjà fait, téléchargez la «salle de TP virtuelle» :

        git clone https://github.com/phillanglois/L3-Algo-Graphes.git 

3.  Allez dans le dossier contenant le matériel pédagogique et lancez JupyterLab. Les
    logiciels requis seront automatiquement installés dans ce dossier.

        cd ~/L3-Algo-Graphes
        uv run jupyter lab

    \% uv run jupyter lab tableau_de_bord.md

La liste des logiciels pourra être mise à jour en en cours de semestre. Dans ce cas:

    cd ~/L3-Algo-Graphes
    git pull
    uv sync
:::

::: {#a36a9fe7-48e6-4208-b5ac-30a9b2088b46 .cell .markdown}
:::{admonition} En savoir un peu plus
:class: dropdown tip

Ce qui suit permet de mieux appréhender l\'architecture logicielle de l\'environnement mis en place par les collègues d\'Orsay.
Il permettra aux curieux de comprendre les évolutions entre l\'environnement classique jupyter utilisé en L1 et celui-ci.

-   [uv](https://docs.astral.sh/uv/) le gestionnaire de paquets python ; les fichiers de la configuration de l\'environnement utilisé sont `pyproject.toml` (lisible et utile) et `uv.lock` (moins lisible)
-   [jupytext](https://jupytext.org) \"remplace\" les fichiers .ipynb par leurs équivalents en .py ou .md exploitables et exécutables sous jupyter ; les fichiers de configurations sont dans `/install_files`
:::

::: {#e1b9ff1b-9f2a-48f2-8f01-1c86a9bbe320 .cell .code}
``` python
```
:::
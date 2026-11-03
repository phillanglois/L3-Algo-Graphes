from typing import Dict, List, Tuple, Optional
from graph import Graph, Node

infinity = float("inf")


def dijkstra(G: Graph, e: Node) -> Tuple[Dict[Node, float], Dict[Node, Optional[Node]]]:
    """
    Applique l'algorithme de Dijkstrat à `G` en partant de `e`
    Renvoie:
    - un dictionnaire associant à chaque sommet sa distance depuis `e`
    - un dictionnaire associant à chaque sommet `v` un autre somment d'où
      vient l'un des chemins les plus courts de `e` à `v`.
    """
    # Remplacer la ligne suivante par le code adéquat
    raise NotImplementedError("code non implanté ligne 17")


def shortest_path(graph: Graph, u: Node, v: Node) -> Tuple[List[Node], float]:
    "Renvoie un plus court chemin de `u` à `v`, ainsi que sa longueur"
    # Remplacer la ligne suivante par le code adéquat
    raise NotImplementedError("code non implanté ligne 23")


# Remplacer la ligne suivante par le code adéquat
# Code non implanté

# -*- coding: utf-8 -*-
"""A home-made class for graphs

This class implements a (tiny) subset of `networkx` features, trying
to retain compatibility, up to some exceptions. For example, the nodes
and edges methods of networkx return views rather than
sequences. Also, the `edges` method is richer in `networkx`, but does
not include the capacity, nor reverse edges for undirected graphs.

We test the compatibility of the basic methods on all the examples:

    >>> import graph, graph_networkx
    >>>
    >>> for G, GN in zip( graph.examples.all(), graph_networkx.examples.all() ):
    ...    assert G.is_directed() == GN.is_directed()
    ...    assert tuple(G.nodes()) == tuple(GN.nodes())
    ...    assert G.number_of_nodes() == GN.number_of_nodes()
    ...    #assert G.number_of_edges() == GN.number_of_edges()
    ...    for v in G.nodes():
    ...        assert set(G.successors(v)) == set(GN.neighbors(v))
    ...    for v1, v2, c in G.edges():
    ...        assert GN.has_edge(v1, v2)
    ...    for v1, v2 in GN.edges():
    ...        assert G.has_edge(v1, v2)
    ...    H = G.networkx()
    ...    assert H.nodes() == GN.nodes()
    ...    assert H.edges() == GN.edges()
    ...    assert H.is_directed() == GN.is_directed()

"""

from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
import networkx  # type: ignore
import graph_examples
from graph_networkx import Node, Capacity, Edge, EdgeList, AdjacencyMatrix


class Graph:

    # Déclaration des attributs
    # La structure de données et l'initialisation vous est donnée
    # pour les sommets (nodes) et pour le choix orienté ou non (directed)

    # Les sommets du graphe
    _nodes: Tuple[Node, ...]
    # Un dictionnaire associant son indice à chaque sommet
    _node_indices: Dict[Node, int]
    _directed: bool

    # À vous de choisir la structure de donnée pour les arêtes (edges)
    ### BEGIN SOLUTION
    _successors: Dict[Node, Dict[Node, Capacity]]
    ### END SOLUTION

    def __init__(
        self,
        nodes: Iterable[Node] = (),
        matrix: Optional[AdjacencyMatrix] = None,
        edges: Optional[EdgeList] = None,
        directed: bool = False,
    ):
        """
        Initialisation d'un graphe

        INPUT :

            - nodes, un itérable sur les sommets du graphe
            - matrix, la matrice d'adjacence du graphe suivant les
              mêmes indices que `nodes`
            - edges, une liste de triplets (v1, v2, c) où v1 et v2
              sont des sommets du graphe et c un nombre positif

        """
        self._nodes = tuple(nodes)
        self._node_indices = {self._nodes[i]: i for i in range(len(self._nodes))}
        self._directed = directed

        # On ne peut pas donner à la fois matrix et edges
        if matrix is not None and edges is not None:
            raise ValueError(
                "'matrix' et 'edges' ne peuvent pas être tous les deux initialisés"
            )

        # Les méthodes _init_xxx sont responsables de
        # l'initialisation de la structure de données
        # pour les arêtes en fonction du type d'entrée
        if matrix is not None:
            self._init_from_matrix(matrix)
        elif edges is not None:
            self._init_from_edges(edges)
        else:
            self._init_empty()

    def _init_empty(self) -> None:
        """
        Initialisation pour un graphe vide (sans arêtes)
        """
        ### BEGIN SOLUTION
        self._successors = {u: {} for u in self._nodes}
        ### END SOLUTION

    def _init_from_matrix(self, matrix: AdjacencyMatrix) -> None:
        """
        Initialisation à partir d'une matrice

        EXAMPLES:

            >>> M = matrix = [[0, 12,  0, 12],
            ...               [0,  0, 23, 0],
            ...               [0,  0,  0, 0],
            ...               [0,  0,  0, 0]]
            >>> G = Graph(nodes = ["A", "B", "C", "D"],
            ...           matrix = M,
            ...           directed = True)
            >>> G.edges()
            (('A', 'B', 12), ('A', 'D', 12), ('B', 'C', 23))
            >>> G.matrix() == M
            True
        """
        ### BEGIN SOLUTION
        edges = [
            (v1, v2, matrix[i1][i2])
            for i1, v1 in enumerate(self._nodes)
            for i2, v2 in enumerate(self._nodes)
            if matrix[i1][i2]
        ]
        self._init_from_edges(edges)
        ### END SOLUTION

    def _init_from_edges(self, edges: EdgeList) -> None:
        """
        Initialisation à partir d'une liste de triplets
        """
        # BEGIN SOLUTION
        self._init_empty()
        for u, v, capacity in edges:
            self._successors[u][v] = capacity
            if not self._directed:
                self._successors[v][u] = capacity
        # END SOLUTION

    def is_directed(self) -> bool:
        """
        Renvoie si le graph est orienté
        """
        return self._directed

    def set_edge_capacity(self, v1: Node, v2: Node, c: Capacity) -> None:
        """
        Donne la capacité `c` à l'arête `(v1,v2)`

        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe
            - c la capacité de l'arête (v1,v2)

        EXAMPLES:

            >>> G = GG = Graph(edges = [(1,2,1)], nodes = [1,2], directed = True)
            >>> G.set_edge_capacity(1,2,2)
            >>> G.edges()
            ((1, 2, 2),)
        """
        # à compléter
        ### BEGIN SOLUTION
        self._successors[v1][v2] = c
        ### END SOLUTION

    def add_node(self, v: Node) -> None:
        """
        Ajoute le sommet `v` au graphe

        INPUT:

            - v, un sommet du graphe

        Complexité:

        ### BEGIN SOLUTION
        ### END SOLUTION
        """
        # à compléter

    def nodes(self) -> Tuple[Node, ...]:
        """
        Renvoie les sommets du graphe

        EXAMPLES::

            >>> from graph import examples
            >>> G = examples.cours_1_reseau()
            >>> G.nodes()
            ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')

        Complexité:

        ### BEGIN SOLUTION
        ### END SOLUTION
        """
        ### BEGIN SOLUTION
        return self._nodes
        ### END SOLUTION

    def number_of_nodes(self) -> int:
        """
        Renvoie le nombre de sommets du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> G.number_of_nodes()
            8

        Complexité:

        ### BEGIN SOLUTION
        ### END SOLUTION
        """
        ### BEGIN SOLUTION
        return len(self._nodes)
        ### END SOLUTION

    def has_node(self, v1: Node) -> bool:
        """
        Renvoie vrai si v1 est un sommet du graphe

        INPUT:

            - v1, un sommet

        Complexité:

        ### BEGIN SOLUTION
        ### END SOLUTION
        """
        return v1 in self._node_indices

    def edges(self) -> Tuple[Edge, ...]:
        """
        Renvoie les arêtes de ce graphe avec leurs capacités

        Chaque arête est renvoyée comme un triplet `(v1, v2, c)`.

        EXAMPLES:

            >>> G = Graph((1,2,3,4))
            >>> G. edges()
            ()
            >>> G = examples.directed()
            >>> sorted(G.edges())
            [(1, 2, 12), (1, 4, 12), (2, 3, 23)]

            >>> G = examples.undirected()
            >>> sorted(G.edges())
            [(1, 2, 12), (2, 1, 12), (2, 3, 23), (3, 2, 23)]

        Complexité:

        ### BEGIN SOLUTION
        ### END SOLUTION
        """
        ### BEGIN SOLUTION
        return tuple(
            (u, v, l) for u, out in self._successors.items() for v, l in out.items()
        )
        ### END SOLUTION

    def number_of_edges(self) -> int:
        """
        Renvoie le nombre d'arêtes du graphe

        Complexité:

        ### BEGIN SOLUTION
        ### END SOLUTION
        """
        ### BEGIN SOLUTION
        return len(self.edges())
        ### END SOLUTION

    def has_edge(self, v1: Node, v2: Node) -> bool:
        """
        Renvoie si l'arête (v1,v2) existe

        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe

        Complexité:

        ### BEGIN SOLUTION
        ### END SOLUTION
        """
        return v2 in self.successors(v1)

    def capacity(self, v1: Node, v2: Node) -> Capacity:
        """
        Renvoie la capacité de l'arête (v1,v2)

        Si l'arête n'existe pas, la capacité est 0.

        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe

        EXAMPLES::

            >>> G = examples.directed()
            >>> G.capacity(1,2)
            12
            >>> G.capacity(2,1)
            0
            >>> G.capacity(2,3)
            23
            >>> G.capacity(3,2)
            0

        Complexité:

        ### BEGIN SOLUTION
        ### END SOLUTION
        """
        ### BEGIN SOLUTION
        return self._successors[v1].get(v2, 0)
        ### END SOLUTION

    def matrix(self) -> List[List[Capacity]]:
        """
        Renvoie la matrice associée au graphe

        Soit `n` le nombre de sommets du graphe. Cette méthode renvoie
        une liste `M` de n listes de taille n, de sorte que `M[i][j]`
        est la capacité de l'arête reliant le i-ème sommet au j-ème
        sommet dans le graphe, s'il y en a une, et 0 sinon.

        EXAMPLES::

            >>> G = examples.directed()
            >>> G.matrix()
            [[0, 12, 0, 12],
             [0, 0, 23, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

        Complexité:

        ### BEGIN SOLUTION
        ### END SOLUTION
        """
        return [[self.capacity(v1, v2) for v2 in self.nodes()] for v1 in self.nodes()]

    def predecessors(self, v: Node) -> Tuple[Node, ...]:
        """
        Renvoie la liste des voisins entrants de `v`

        INPUT:

            - v, un sommet du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> sorted(G.predecessors("H"))
            ['C', 'D', 'E', 'G']
            >>> G = examples.directed()
            >>> G.predecessors(1)
            ()
            >>> G.predecessors(2)
            (1,)

        Complexité:

        ### BEGIN SOLUTION
        ### END SOLUTION
        """
        ### BEGIN SOLUTION
        return tuple(u for u in self._nodes if v in self._successors[u])
        ### END SOLUTION

    def successors(self, v: Node) -> Tuple[Node, ...]:
        """
        Renvoie la liste des voisins sortants de `v`

        INPUT:

            - v, un sommet du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> sorted(G.successors("A"))
            ['B', 'F', 'G']
            >>> G = examples.directed()
            >>> sorted(G.successors(1))
            [2, 4]
            >>> G.successors(2)
            (3,)
            >>> G.successors(4)
            ()

        Complexité:

        ### BEGIN SOLUTION
        ### END SOLUTION
        """
        ### BEGIN SOLUTION
        return tuple(self._successors[v].keys())
        ### END SOLUTION

    neighbors = successors

    def is_path(self, p: Sequence[Node]) -> bool:
        """
        Renvoie si `p` est un chemin valide dans le graphe

        INPUT:

            - p, une liste de sommets du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> G.is_path([])
            True
            >>> G.is_path(["D"])
            True
            >>> G.is_path(["D", "G"])
            False
            >>> G.is_path(["D", "H"])
            True
            >>> G.is_path(["D", "H", "F"])
            False
            >>> G.is_path(["D", "H", "G", "B", "A"])
            True

        Complexité:

        ### BEGIN SOLUTION
        ### END SOLUTION
        """
        ### BEGIN SOLUTION
        for i in range(len(p) - 1):
            if not self.has_edge(p[i], p[i + 1]):
                return False
        return True
        ### END SOLUTION

    def networkx(self) -> networkx.Graph:
        """
        Return a networkx graph with the same nodes and edges
        """
        import graph_networkx

        return graph_networkx.Graph(
            self.nodes(), self.edges(), directed=self.is_directed()
        )

    def show(self) -> Any:
        """
        Display the current graph
        """
        return self.networkx().show()


examples = graph_examples.Examples(Graph)

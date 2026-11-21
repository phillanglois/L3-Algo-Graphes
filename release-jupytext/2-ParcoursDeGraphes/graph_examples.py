from typing import Any, Callable, List

Graph = Any


class Examples:
    """
    Une collection de graphes, pour tests, ...
    """

    def __init__(self, Graph: Callable) -> None:
        self.Graph = Graph

    def C3(self) -> Graph:
        return self.Graph(
            (0, 1, 2), edges=((0, 1, 1), (1, 2, 1), (2, 0, 1)), directed=True
        )

    def C5(self) -> Graph:
        return self.Graph(
            (0, 1, 2, 3, 4),
            edges=((0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 0, 1)),
            directed=True,
        )

    def T3(self) -> Graph:
        return self.Graph(
            (0, 1, 2), edges=((0, 1, 1), (0, 2, 1), (1, 2, 1)), directed=True
        )

    def cours_1_G(self) -> Graph:
        return self.Graph(
            (0, 1, 2, 3, 4, 5),
            edges=((0, 2, 1), (1, 2, 1), (2, 3, 1), (1, 5, 1), (5, 3, 1), (3, 4, 1)),
        )

    def complet(self, n: int) -> Graph:
        return self.Graph(
            nodes=list(range(n)),
            edges=[(u, v, 1) for u in range(n) for v in range(n) if v != u],
        )

    def parcours_directed(self) -> Graph:
        A, B, C, D, E, F, G, H = nodes = "A", "B", "C", "D", "E", "F", "G", "H"
        return self.Graph(
            nodes,
            edges=(
                (A, B, 3),
                (A, G, 2),
                (A, F, 4),
                (B, C, 1),
                (B, G, 1),
                (C, D, 4),
                (C, G, 5),
                (C, H, 2),
                (D, H, 6),
                (H, F, 6),
                (E, F, 3),
                (E, G, 2),
                (E, H, 3),
                (F, G, 1),
                (G, H, 4),
            ),
            directed=True,
        )

    def cours_1_reseau(self) -> Graph:
        A, B, C, D, E, F, G, H = nodes = list("ABCDEFGH")
        return self.Graph(
            nodes,
            edges=(
                (A, B, 3),
                (A, G, 2),
                (A, F, 4),
                (B, C, 1),
                (B, G, 1),
                (C, D, 4),
                (C, G, 5),
                (C, H, 2),
                (D, E, 5),
                (D, H, 6),
                (E, F, 3),
                (E, G, 2),
                (E, H, 3),
                (F, G, 1),
                (G, H, 4),
            ),
            directed=False,
        )

    def dijkstra(self) -> Graph:
        A, B, C, D, E, F, G, H, I, J = nodes = list("ABCDEFGHIJ")
        return self.Graph(
            nodes=nodes,
            edges=[
                (A, B, 87),
                (A, C, 217),
                (A, E, 173),
                (B, F, 80),
                (C, G, 186),
                (C, H, 103),
                (D, H, 183),
                (E, J, 502),
                (F, I, 250),
                (H, J, 167),
                (I, J, 84),
            ],
        )

    def cours_2_reseau(self) -> Graph:
        return self.Graph(
            nodes=list(range(7)),
            edges=[
                (0, 1, 1),
                (0, 2, 2),
                (0, 3, 1),
                (1, 4, 3),
                (2, 1, 1),
                (2, 0, 1),
                (2, 4, 1),
                (3, 5, 2),
                (4, 6, 5),
                (5, 2, 1),
                (5, 6, 4),
                (6, 3, 3),
            ],
            directed=True,
        )

    def directed(self) -> Graph:
        return self.Graph(
            (1, 2, 3, 4), edges=((1, 2, 12), (1, 4, 12), (2, 3, 23)), directed=True
        )

    def undirected(self) -> Graph:
        return self.Graph((1, 2, 3, 4), edges=((1, 2, 12), (2, 3, 23)))

    def disconnected(self) -> Graph:
        return self.Graph(
            (1, 2, 3, 4, 5), edges=((1, 2, "12"), (2, 5, "25"), (3, 4, "34"))
        )

    def all(self) -> List[Graph]:
        return [
            self.C3(),
            self.T3(),
            self.cours_1_G(),
            self.cours_1_reseau(),
            self.directed(),
            self.undirected(),
            self.disconnected(),
            self.dijkstra(),
        ]

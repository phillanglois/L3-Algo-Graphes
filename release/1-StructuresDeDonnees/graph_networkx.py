"""
Some utilities on top of networkx

- A convenient constructor
- Display with bqplot
- types
- examples
"""

from typing import Any, Dict, Optional, Sequence, Tuple, cast
import warnings
import networkx  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

import graph_examples

Node = Any
Capacity = Any
Edge = Tuple[Node, Node, Capacity]
EdgeList = Sequence[Edge]
EdgeDict = Dict[Tuple[Node, Node], Capacity]
AdjacencyMatrix = Sequence[Sequence[Capacity]]
NeighborDict = Dict[Node, Sequence[Tuple[Node, Capacity]]]


def Graph(
    nodes: Sequence[Node], edges: Optional[EdgeList] = None, directed: bool = False
) -> networkx.Graph:
    if directed:
        G = networkx.DiGraph()
    else:
        G = networkx.Graph()
    G.add_nodes_from(nodes)
    if edges:
        if len(edges[0]) == 2:
            G.add_edges_from(edges)
        else:
            G.add_weighted_edges_from(edges)
    return G


def default_layout(self: networkx.Graph) -> Dict:
    try:
        # ignore a FutureWarning in numpy raised
        # by networkx's planar_layout
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            return cast(Dict, networkx.planar_layout(self))
    except networkx.NetworkXException:
        return cast(Dict, networkx.spring_layout(self))


def show(self: networkx.Graph) -> Any:
    edge_labels = {(u, v): w for u, v, w in self.edges.data("weight")}
    edge_labels = {
        (u, v): w for (u, v), w in edge_labels.items() if w is not None and w != 1
    }
    layout = default_layout(self)

    plt.figure()
    networkx.draw(
        self,
        layout,
        width=3,
        linewidths=1,
        node_size=500,
        node_color="lightgray",
        alpha=0.9,
        labels={node: node for node in self.nodes()},
    )
    networkx.draw_networkx_edge_labels(
        self, layout, edge_labels=edge_labels, font_color="black"
    )
    plt.axis("off")
    plt.show()


def show_bqplot(self: Any) -> Any:
    """
    Return a bqplot widget representing the graph
    """
    import bqplot.marks  # type: ignore
    from ipywidgets import Layout  # type: ignore

    nodes = self.nodes()
    edges = self.edges()
    node_data = [str(i) for i in nodes]
    rank = {v: i for i, v in enumerate(nodes)}
    link_data = [
        {
            "source": rank[edge[0]],
            "target": rank[edge[1]],
        }
        for edge in edges
    ]
    colors = ["white" for node in nodes]

    layout = default_layout(self)

    xs = bqplot.LinearScale()
    ys = bqplot.LinearScale()
    x = [layout[node][0] for node in nodes]
    y = [layout[node][1] for node in nodes]

    fig_layout = Layout(width="400px", height="400px")
    mark = bqplot.marks.Graph(
        node_data=node_data,
        link_data=link_data,
        link_type="line",
        directed=self.is_directed(),
        scales={
            "x": xs,
            "y": ys,
        },
        x=x,
        y=y,
        colors=colors,
        charge=-600,
    )
    return bqplot.Figure(marks=[mark], layout=fig_layout)


def set_edge_capacity(self: Any, v1: Node, v2: Node, c: Capacity) -> None:
    """
    Donne la capacité `c` à l'arête `(v1,v2)`

    INPUT:

        - v1, un sommet du graphe
        - v2, un sommet du graphe
        - c la capacité de l'arête (v1,v2)
    """
    if v2 not in self[v1]:
        self.add_edge(v1, v2, weight=c)
    else:
        self[v1][v2]["weight"] = c


def capacity(self: Any, v1: Node, v2: Node) -> Capacity:
    """
    Renvoie la capacité de l'arête (v1,v2)

    Si l'arête n'existe pas, la capacité est 0.

    INPUT:

        - v1, un sommet du graphe
        - v2, un sommet du graphe
    """
    if v2 not in self[v1]:
        return 0
    if "weight" not in self[v1][v2]:
        return 1
    return self[v1][v2]["weight"]


networkx.Graph.show = show
networkx.Graph.set_edge_capacity = set_edge_capacity
networkx.Graph.capacity = capacity

examples = graph_examples.Examples(Graph)

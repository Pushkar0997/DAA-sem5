from typing import Any, Dict, List, Set, Tuple


class DisjointSetUnion:
    """Disjoint Set Union (DSU) / Union-Find with Path Compression and Union by Rank."""

    def __init__(self, elements: Set[Any]):
        self.parent: Dict[Any, Any] = {elem: elem for elem in elements}
        self.rank: Dict[Any, int] = {elem: 0 for elem in elements}

    def find(self, item: Any) -> Any:
        """Finds the root representative of the set containing item (with Path Compression)."""
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, item1: Any, item2: Any) -> bool:
        """Unites the sets containing item1 and item2 (Union by Rank).

        Returns True if merged, False if both were already in the same set (cycle detected).
        """
        root1 = self.find(item1)
        root2 = self.find(item2)

        if root1 == root2:
            return False  # Cycle detected

        # Attach smaller rank tree under root of higher rank tree
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        return True


def kruskals_mst(
    nodes: List[Any], edges: List[Tuple[Any, Any, float]]
) -> Tuple[float, List[Tuple[Any, Any, float]]]:
    """Computes the Minimum Spanning Tree (MST) using Kruskal's Algorithm.

    :param nodes: List of all node identifiers
    :param edges: List of tuples (node1, node2, weight)
    :return: (total_mst_weight, list_of_mst_edges)
    """
    # 1. Sort all edges non-decreasingly by weight: O(E log E)
    sorted_edges = sorted(edges, key=lambda edge: edge[2])

    dsu = DisjointSetUnion(set(nodes))
    mst_edges = []
    total_weight = 0.0

    # 2. Iterate through sorted edges and greedily unite disjoint components
    for u, v, weight in sorted_edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight

            # Early termination: An MST on V nodes has exactly V - 1 edges
            if len(mst_edges) == len(nodes) - 1:
                break

    # 3. Connectivity check
    if len(nodes) > 1 and len(mst_edges) != len(nodes) - 1:
        raise ValueError(
            "Graph is disconnected! An MST cannot span all nodes."
        )

    return total_weight, mst_edges


def main():
    print("--- Kruskal's MST Algorithm ---")
    try:
        raw_v = input("Enter total number of nodes (V): ").strip()
        V = int(raw_v)

        raw_e = input("Enter total number of edges (E): ").strip()
        E = int(raw_e)

        print(
            "\nEnter each edge in format: `node1 node2 weight` (e.g., `A B 5` or `0 1 10`):"
        )
        edges = []
        observed_nodes = set()

        for i in range(E):
            line = input(f"Edge {i + 1}: ").strip().replace("'", "").replace('"', "")
            parts = line.split()

            if len(parts) != 3:
                raise ValueError(
                    f"Invalid input '{line}'. Expected 3 items: node1 node2 weight."
                )

            u, v, w_str = parts[0], parts[1], parts[2]
            w = float(w_str) if "." in w_str else int(w_str)

            edges.append((u, v, w))
            observed_nodes.add(u)
            observed_nodes.add(v)

        nodes = list(observed_nodes)

        if len(nodes) != V:
            print(
                f"\n[!] Note: You specified V={V}, but provided edges containing {len(nodes)} distinct nodes: {nodes}"
            )

        total_weight, mst_edges = kruskals_mst(nodes, edges)

        print("\n[+] --- Minimum Spanning Tree Result ---")
        print(f"Total MST Cost/Weight: {total_weight}")
        print("Included Edges:")
        for u, v, w in mst_edges:
            print(f"  * Node {u} <---> Node {v}  | Weight: {w}")

    except ValueError as err:
        print(f"\n[!] Error: {err}")


if __name__ == "__main__":
    main()
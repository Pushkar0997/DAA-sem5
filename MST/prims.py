import heapq
from collections import defaultdict
from typing import Any, Dict, List, Tuple


def prims_mst(
    nodes: List[Any], edges: List[Tuple[Any, Any, float]]
) -> Tuple[float, List[Tuple[Any, Any, float]]]:
    """Computes the Minimum Spanning Tree (MST) using Prim's Algorithm.

    Supports arbitrary node labels (characters, strings, or integers).
    """
    # 1. Build Adjacency List
    adj: Dict[Any, List[Tuple[float, Any]]] = defaultdict(list)
    for u, v, weight in edges:
        adj[u].append((weight, v))
        adj[v].append((weight, u))

    # 2. Tracking structures
    visited = set()
    mst_edges = []
    total_weight = 0.0

    # Pick the first defined node as the starting root
    start_node = nodes[0]
    min_heap = [(0.0, start_node, None)]

    while min_heap and len(visited) < len(nodes):
        weight, u, parent = heapq.heappop(min_heap)

        if u in visited:
            continue

        visited.add(u)
        total_weight += weight

        if parent is not None:
            mst_edges.append((parent, u, weight))

        for edge_weight, neighbor in adj[u]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, u))

    # Validate graph connectivity
    if len(visited) != len(nodes):
        raise ValueError(
            "Graph is disconnected! An MST cannot span all nodes."
        )

    return total_weight, mst_edges


def main():
    print("--- Prim's MST Algorithm ---")
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

        total_weight, mst_edges = prims_mst(nodes, edges)

        print("\n[+] --- Minimum Spanning Tree Result ---")
        print(f"Total MST Cost/Weight: {total_weight}")
        print("Included Edges:")
        for u, v, w in mst_edges:
            print(f"  * Node {u} <---> Node {v}  | Weight: {w}")

    except ValueError as err:
        print(f"\n[!] Error: {err}")


if __name__ == "__main__":
    main()
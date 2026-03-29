#!/usr/bin/env python3
"""graph_color: Graph coloring (greedy + backtracking)."""
import sys

def greedy_color(adj):
    n = len(adj)
    colors = [-1] * n
    for node in range(n):
        used = {colors[nb] for nb in adj[node] if colors[nb] != -1}
        c = 0
        while c in used: c += 1
        colors[node] = c
    return colors

def backtrack_color(adj, k):
    n = len(adj)
    colors = [-1] * n
    def solve(node):
        if node == n: return True
        for c in range(k):
            if all(colors[nb] != c for nb in adj[node] if colors[nb] != -1):
                colors[node] = c
                if solve(node + 1): return True
                colors[node] = -1
        return False
    return colors if solve(0) else None

def chromatic_number(adj):
    for k in range(1, len(adj) + 1):
        if backtrack_color(adj, k) is not None:
            return k
    return len(adj)

def test():
    # Triangle (K3) needs 3 colors
    adj = [[1,2],[0,2],[0,1]]
    c = greedy_color(adj)
    for i in range(3):
        for j in adj[i]:
            assert c[i] != c[j]
    assert chromatic_number(adj) == 3
    # Bipartite (K2,2) needs 2
    adj2 = [[2,3],[2,3],[0,1],[0,1]]
    assert chromatic_number(adj2) == 2
    # Single node
    assert chromatic_number([[]]) == 1
    # Path graph
    adj3 = [[1],[0,2],[1]]
    assert chromatic_number(adj3) == 2
    # K4
    adj4 = [[1,2,3],[0,2,3],[0,1,3],[0,1,2]]
    assert chromatic_number(adj4) == 4
    print("All tests passed!")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print("Usage: graph_color.py test")

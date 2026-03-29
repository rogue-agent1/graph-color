#!/usr/bin/env python3
"""graph_color - Graph coloring algorithms (greedy, backtracking)."""
import sys

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def greedy_color(self):
        colors = [-1]*self.n
        for u in range(self.n):
            used = set(colors[v] for v in self.adj[u] if colors[v] != -1)
            c = 0
            while c in used:
                c += 1
            colors[u] = c
        return colors

    def backtrack_color(self, k):
        colors = [-1]*self.n
        if self._bt(colors, 0, k):
            return colors
        return None

    def _bt(self, colors, node, k):
        if node == self.n:
            return True
        for c in range(k):
            if all(colors[v] != c for v in self.adj[node]):
                colors[node] = c
                if self._bt(colors, node + 1, k):
                    return True
                colors[node] = -1
        return False

    def chromatic_number(self):
        for k in range(1, self.n + 1):
            if self.backtrack_color(k) is not None:
                return k
        return self.n

def test():
    g = Graph(5)
    g.add_edge(0,1); g.add_edge(0,2); g.add_edge(1,2)
    g.add_edge(1,3); g.add_edge(2,4); g.add_edge(3,4)
    colors = g.greedy_color()
    for u in range(5):
        for v in g.adj[u]:
            assert colors[u] != colors[v]
    result = g.backtrack_color(3)
    assert result is not None
    for u in range(5):
        for v in g.adj[u]:
            assert result[u] != result[v]
    tri = Graph(3)
    tri.add_edge(0,1); tri.add_edge(1,2); tri.add_edge(0,2)
    assert tri.chromatic_number() == 3
    assert tri.backtrack_color(2) is None
    ind = Graph(3)
    assert ind.chromatic_number() == 1
    print("All tests passed!")

if __name__ == "__main__":
    test() if "--test" in sys.argv else print("graph_color: Graph coloring. Use --test")

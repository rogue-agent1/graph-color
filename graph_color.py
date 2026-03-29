#!/usr/bin/env python3
"""graph_color - Graph coloring with greedy and backtracking algorithms."""
import sys
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(set)
    def add_edge(self, u, v):
        self.adj[u].add(v); self.adj[v].add(u)
    @property
    def nodes(self): return set(self.adj.keys())

def greedy_color(g):
    colors = {}
    for node in sorted(g.nodes):
        used = {colors[n] for n in g.adj[node] if n in colors}
        c = 0
        while c in used: c += 1
        colors[node] = c
    return colors

def is_valid(g, colors):
    for u in g.nodes:
        for v in g.adj[u]:
            if u in colors and v in colors and colors[u] == colors[v]:
                return False
    return True

def chromatic_backtrack(g, max_colors):
    nodes = sorted(g.nodes)
    colors = {}
    def bt(i):
        if i == len(nodes): return True
        node = nodes[i]
        for c in range(max_colors):
            if all(colors.get(n) != c for n in g.adj[node]):
                colors[node] = c
                if bt(i + 1): return True
                del colors[node]
        return False
    return colors if bt(0) else None

def test():
    g = Graph()
    for u, v in [(0,1),(1,2),(2,3),(3,0),(0,2)]:
        g.add_edge(u, v)
    c = greedy_color(g)
    assert is_valid(g, c)
    assert max(c.values()) <= 3
    c2 = chromatic_backtrack(g, 3)
    assert c2 is not None and is_valid(g, c2)
    c3 = chromatic_backtrack(g, 2)
    assert c3 is None  # K4 minus edge needs 3
    print("graph_color: all tests passed")

if __name__ == "__main__":
    test() if "--test" in sys.argv else print("Usage: graph_color.py --test")

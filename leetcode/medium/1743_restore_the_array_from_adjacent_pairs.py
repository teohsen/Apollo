from typing import List
from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        adjs = defaultdict(set)
        for u, v in adjacentPairs:
            adjs[u].add(v)
            adjs[v].add(u)

        for node, adj in adjs.items():
            if len(adj).__eq__(1):
                break

        ans=[node]
        while adjs[node]:
            new=adjs[node].pop()
            ans.append(new)
            adjs[new].remove(node)
            node=new
        return ans


    def test(self):
        input = [[2,1],[3,4],[3,2]]
        answer = [1,2,3,4]

        result = self.restoreArray(input)

        assert result == answer




"""
Throwing to ChatGPT

To solve this problem, you can use a hash table to build a graph of adjacent elements and then perform a 
depth-first search (DFS) to reconstruct the original array. Here's a Python implementation:

from collections import defaultdict

def restoreArray(adjacentPairs):
    graph = defaultdict(list)

    # Build the graph
    for pair in adjacentPairs:
        u, v = pair
        graph[u].append(v)
        graph[v].append(u)

    # Find the start node (a node with only one neighbor)
    start_node = None
    for node, neighbors in graph.items():
        if len(neighbors) == 1:
            start_node = node
            break

    # Perform DFS to reconstruct the array
    def dfs(node, visited):
        visited.add(node)
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    visited = set()
    result = []
    dfs(start_node, visited)

    return result

# Example usage:
adjacentPairs = [[2, 1], [3, 4], [3, 2]]
result = restoreArray(adjacentPairs)
print(result)

"""
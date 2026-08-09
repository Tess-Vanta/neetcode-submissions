class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        vis = [False] * n

        def dfs(node, parent):
            vis[node] = True

            for next_node in adj[node]:
                if next_node == parent:
                    continue
                if vis[next_node]:
                    return False
                if not dfs(next_node, node):
                    return False

            return True
        
        if not dfs(0, -1):
            return False

        return all(vis)

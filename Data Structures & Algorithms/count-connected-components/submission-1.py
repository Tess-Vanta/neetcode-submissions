class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        vis = [False] * n
        def dfs(node):
            vis[node] = True
            for nn in adj[node]:
                if not vis[nn]:
                    dfs(nn)
        
        res = 0
        for i in range(n):
            if not vis[i]:
                res += 1
                if dfs(i):
                    continue 
        return res
            

from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]],
                       s: str, queries: List[str]) -> List[bool]:

        # Build the tree.
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        # Find parents and depths using iterative DFS.
        order = [0]
        for u in order:
            for v in graph[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        # Calculate subtree sizes and heavy children.
        for u in reversed(order):
            largest = 0
            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        current_pos = 0

        # Decompose the tree into heavy chains.
        stack = [(0, 0)]
        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = current_pos
                current_pos += 1

                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        # Store each character as a 26-bit mask.
        base = 1
        while base < n:
            base *= 2

        seg = [0] * (2 * base)
        chars = list(s)

        for u in range(n):
            seg[base + pos[u]] = 1 << (ord(chars[u]) - ord('a'))

        # Build the XOR segment tree.
        for i in range(base - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def update(node, value):
            i = base + pos[node]
            seg[i] = value
            i //= 2

            while i:
                seg[i] = seg[2 * i] ^ seg[2 * i + 1]
                i //= 2

        def range_xor(left, right):
            result = 0
            left += base
            right += base

            while left <= right:
                if left % 2 == 1:
                    result ^= seg[left]
                    left += 1

                if right % 2 == 0:
                    result ^= seg[right]
                    right -= 1

                left //= 2
                right //= 2

            return result

        def path_xor(u, v):
            result = 0

            # Process heavy-chain segments until both nodes
            # belong to the same chain.
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(pos[head[u]], pos[u])
                u = parent[head[u]]

            # Process the final segment on the shared chain.
            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v])
            return result

        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                chars[u] = c
                update(u, 1 << (ord(c) - ord('a')))

            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_xor(u, v)

                # At most one character may have an odd frequency.
                answer.append((mask & (mask - 1)) == 0)

        return answer

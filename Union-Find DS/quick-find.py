
class UnionFindDS(object):
    def __init__(self, n: int) -> None:
        self.ids = [identifier for identifier in range(n)]

    def __str__(self):
        nodes = [node for node in range(len(self.ids))]
        return f"Nodes-Indexes:\n{nodes}\n{self.ids}"

    def connected(self, p: int, q: int) -> bool:
        return self.ids[p] == self.ids[q]

    def union(self, p: int, q: int) -> None:
        idp = self.ids[p]
        idq = self.ids[q]
        for identifier in self.ids:
            if identifier == idp:
                self.ids[p] = idq


if __name__ == "__main__":
    N = 10
    uf = UnionFindDS(N)
    print(uf.connected(1, 2))
    uf.union(1, 2)
    print(uf)
    uf.union(9, 2)
    print(uf)

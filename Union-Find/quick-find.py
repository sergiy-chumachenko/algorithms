
class UnionFindDS(object):
    def __init__(self, n: int) -> None:
        self.ids = [identifier for identifier in range(n)]

    def __str__(self):
        return f"Nodes: {[i for i in range(len(self.ids))]}\nIds:   {self.ids}\n"

    def connected(self, p: int, q: int) -> bool:
        """
        Check if P and Q have the same id
        """
        return self.ids[p] == self.ids[q]

    def union(self, p: int, q: int) -> None:
        """
        To merge components containing p and q, change all entries whose ID equals id[p] to id[q]
        """
        pid = self.ids[p]
        qid = self.ids[q]

        for identifier in self.ids:
            if identifier == pid:
                self.ids[self.ids.index(identifier)] = qid


if __name__ == "__main__":
    N = 10
    uf = UnionFindDS(N)
    print(uf.connected(1, 2))
    uf.union(1, 2)
    print(uf)
    uf.union(9, 2)
    print(uf)
    uf.union(3, 4)
    print(uf)
    uf.union(9, 4)
    print(uf)


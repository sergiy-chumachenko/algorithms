
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
        print(f"Union: {p}, {q}")
        pid = self.ids[p]
        qid = self.ids[q]

        for identifier in self.ids:
            if identifier == pid:
                self.ids[self.ids.index(identifier)] = qid


if __name__ == "__main__":
    uf = UnionFindDS(10)
    for union in [
        (1, 2),
        (6, 2),
        (7, 2),
        (1, 9),
        (0, 9),
        (0, 5),
        (3, 4),
        (3, 8),
        (0, 8)
    ]:
        uf.union(*union)
        print(uf)


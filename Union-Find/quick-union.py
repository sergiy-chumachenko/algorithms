class UnionFind:
    def __init__(self, n: int) -> None:
        self.ids = [identifier for identifier in range(n)]

    def __root(self, i: int) -> int:
        """Find root of component"""
        while i != self.ids[i]:
            i = self.ids[i]
        return i

    def connected(self, p: int, q: int) -> bool:
        """Check if p and q have the same root"""
        return self.__root(p) == self.__root(q)

    def union(self, p: int, q: int) -> None:
        """To merge components containing p and q set the id of p's root to the id of q's root"""
        print(f"Union: {p}, {q}")
        i = self.__root(p)
        j = self.__root(q)
        self.ids[i] = j

    def __str__(self):
        return f"Nodes: {[i for i in range(len(self.ids))]}\nIds:   {self.ids}\n"


if __name__ == "__main__":
    uf = UnionFind(10)
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

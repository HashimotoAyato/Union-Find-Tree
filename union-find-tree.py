class UnionFind:
    # 初期化
    def __init__(self, max_n):
        self.parent = [] # 親(初期値は自分自信)
        self.rank = [] # 木の高さ(初期値0)
        for i in range(max_n):
            self.parent.append(i)
            self.rank.append(0)

    # xの木の根を求める
    def find(self, x):
        if self.parent[x] == x:
            # 根を到達
            return x
        else:
            # 求まった根を用いて、辺の縮約
            self.parent[x] = self.find(self.parent[x])
            # 親の親を返す
            return self.parent[x]

    # xとyが属するグループを併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    
    # xとyが同じグループに属するか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)
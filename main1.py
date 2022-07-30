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
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

# below is slove

N, K = map(int, input().split())
# union-find tree
uf = UnionFind(N*3)

error = 0
for i in range(K):
    type, x, y = map(int, input().split())
    x -= 1
    y -= 1

    # input is incorrect
    if x < 0 or N <= x or y < 0 or N <= y:
        error += 1
        continue

    # type 1
    if type == 1:
        if uf.same(x, y+N) or uf.same(x, y+N*2):
            error += 1
        else:
            uf.union(x, y)
            uf.union(x+N, y+N)
            uf.union(x+N*2, y+N*2) 
    # type 2       
    else:
        if uf.same(x, y) or uf.same(x, y+2*N):
            error += 1
        else:
            uf.union(x, y+N)
            uf.union(x+N, y+2*N)
            uf.union(x+2*N, y)

print('ans = {}'.format(error))

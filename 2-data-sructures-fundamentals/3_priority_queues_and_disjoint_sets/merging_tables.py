class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        self.parents[src_parent] = dst_parent
        self.row_counts[dst_parent] +=  self.row_counts[src_parent]
        self.row_counts[src_parent] = 0
        if self.max_row_count < self.row_counts[dst_parent]:
            self.max_row_count = self.row_counts[dst_parent]
        
        return True

    def get_parent(self, table):
        # find parent and compress path
        if table != self.parents[table]:
            self.parents[table] = self.get_parent(self.parents[table])

        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)

    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(src - 1, dst - 1)
        print(db.max_row_count)
        #print("Parents:", db.parents)
        #print("Size:", db.row_counts)

if __name__ == "__main__":
    main()

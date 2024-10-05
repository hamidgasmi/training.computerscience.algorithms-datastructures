

export class UnionFindRankHeuristic {
    private _rank: number[]
    private _parent: number[]

    public constructor(size: number) {
        this._rank = []
        this._parent = []

        for(let i = 0; i < size; i++) {
            this._rank.push(0)
            this._parent.push(i)
        }
    }

    public find(i: number): number {
        if (i < 0 || i >= this._parent.length) {
            return -1
        }

        let iRoot = i
        while (iRoot !== this._parent[iRoot]) {
            iRoot = this._parent[iRoot]
        }

        return iRoot
    }

    public union(i: number, j: number): void {
        let iRoot = this.find(i)
        let jRoot = this.find(j)
        if (iRoot === jRoot) {
            return
        }

        if (this._rank[iRoot] < this._rank[jRoot]) {
            this._parent[iRoot] = jRoot

        } else {
            this._parent[jRoot] = iRoot

            if (this._rank[iRoot] === this._rank[jRoot]) {
                this._rank[iRoot] += 1
            }
        }
    }
}
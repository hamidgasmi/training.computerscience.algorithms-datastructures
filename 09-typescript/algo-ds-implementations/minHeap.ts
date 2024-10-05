export class MinHeap<T> {
    private _priorityQueue: T[]

    // Time Complexity: O(n)
    public static build<U>(arr: U[] = []): MinHeap<U> {
        const minHeap = new MinHeap<U>()
        minHeap.priorityQueue = arr.map(v => v)

        for (let i = Math.floor(arr.length / 2); i > -1; i--) {
            minHeap.siftDown(i)
        }

        return minHeap
    }

    public constructor() {
        this._priorityQueue = []
    }

    public getLeft(i: number): number {
        if (!this._isValidIndex(i)) {
            return - 1
        }

        const l = 2 * i + 1
        return this._isValidIndex(l) ? l : -1
    }

    public getRight(i: number): number {
        if (!this._isValidIndex(i)) {
            return - 1
        }

        const r = 2 * i + 2
        return this._isValidIndex(r) ? r : -1
    }

    public getParent(i: number): number {
        if (i === 0 || !this._isValidIndex(i)) {
            return - 1
        }

        return Math.floor((i - 1) / 2)
    }

    // Time Complexity: O(1)
    public getMin(): T | undefined {
        return this.getElement(0)
    }

    // Time Complexity: O(1)
    public getElement(i: number): T | undefined {
        if (!this._isValidIndex(i)) {
            return undefined
        }

        return this._priorityQueue.at(i)
    }

    // Time Complexity: O(Log(n))
    public extractMin(): T | undefined {
        if (this._priorityQueue.length < 2) {
            return this._priorityQueue.pop()
        }

        const minVal = this._priorityQueue[0]
        this._priorityQueue[0] = this._priorityQueue.pop() as T

        this.siftDown(0)

        return minVal
    }

    // Time Complexity: O(Log(n))
    public insert(val: T): void {
        this._priorityQueue.push(val)
        this.siftUp(this._priorityQueue.length - 1)
    }

    // Time Complexity: O(Log(n))
    public siftDown(i: number): void {
        if (!this._isValidIndex(i)) {
            return
        }

        let p = i
        let minIndex = i
        
        do {
            p = minIndex

            const lc = this.getLeft(p)
            const rc = this.getRight(p)

            if (lc > 0 && this._priorityQueue[lc] < this._priorityQueue[minIndex]) {
                minIndex = lc
            }
            
            if (rc > 0 && this._priorityQueue[rc] < this._priorityQueue[minIndex]) {
                minIndex = rc
            }

            [ this._priorityQueue[p], this._priorityQueue[minIndex] ] = [ this._priorityQueue[minIndex], this._priorityQueue[p] ]
    
        } while (p !== minIndex)
    }

    // Time Complexity: O(Log(n))
    public siftUp(i: number): void {
        if (!this._isValidIndex(i)) {
            return
        }

        let c = i
        let p = this.getParent(i)

        while (p >= 0 && this._priorityQueue[c] < this._priorityQueue[p]) {
            [ this._priorityQueue[p], this._priorityQueue[c] ] = [ this._priorityQueue[c], this._priorityQueue[p] ]

            c = p
            p = this.getParent(p)
        } 
    }

    public get size(): number {
        return this._priorityQueue.length
    }

    public toString(): string {
        return this._priorityQueue.join(',')
    }

    private set priorityQueue(arr: T[]) {
        this._priorityQueue = arr
    }
    private _isValidIndex(i: number): boolean {
        return i >= 0 && i < this._priorityQueue.length
    }
}
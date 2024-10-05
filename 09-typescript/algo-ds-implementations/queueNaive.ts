/*
    Naive implementation:
        enQueue: O(1)
        deQueue: (N)
    
    Better Approach: Use Doubly Linked List instead
*/
export class Queue<T> {
    private _queue: T[]
    
    public constructor() {
        this._queue = []
    }

    public enQueue(value: T): void {
        this._queue.push(value)
    }

    public deQueue(): T | undefined {
        return this._queue.shift()
    }

    public get size(): number { 
        return this._queue.length
    }

    public toString(): string { 
        return this._queue.join(',')
    }
}

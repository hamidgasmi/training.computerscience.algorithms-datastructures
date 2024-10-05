export class Queue<T> {
    private _size: number
    private _likedList: DoublyLinkedList<T>
    
    public constructor() {
        this._size = 0
        this._likedList = new DoublyLinkedList<T>()
    }

    public enQueue(value: T): void {
        this._size += 1
        this._likedList.pushBack(value)
    }

    public deQueue(): T | undefined {
        if (this._size > 0) {
            this._size -= 1
        }

        return this._likedList.popFront()
    }

    public get size(): number { 
        return this._size
    }

    public toString(): string { 
        return this._likedList.toString()
    }
}

export interface DoublyLinkedNode<T> {
    next: DoublyLinkedNode<T> | null,
    prev: DoublyLinkedNode<T> | null,
    value: T
}

export class DoublyLinkedList<T> {
    private _head: DoublyLinkedNode<T> | null
    private _tail: DoublyLinkedNode<T> | null

    public constructor() {
        this._head = null
        this._tail = null
    }

    public get isEmpty(): boolean {
        return this._head === null
    }

    public pushBack(value: T): void {
        const newTail: DoublyLinkedNode<T> = { next: null, prev: this._tail, value }

        if (this.isEmpty) {
            this._head = newTail
        } else {
            this._tail!.next = newTail
        }

        this._tail = newTail
    }

    public popFront(): T | undefined {
        if (this.isEmpty) {
            return undefined
        }

        const value = this._head!.value

        if (this._head === this._tail) {
            this._head = null
            this._tail = null

        } else {
            const newHead = this._head!.next!

            newHead.prev = null
            this._head = newHead
        }


        return value
    }

    public toString(): string {
        const values: T[] = []

        let node = this._head

        while (node) {
            values.push(node.value)

            node = node.next
        }

        return values.join(',')
    }
}

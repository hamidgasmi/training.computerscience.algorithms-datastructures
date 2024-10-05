export interface DoublyLinkedNode<T> {
    next: DoublyLinkedNode<T> | null,
    prev: DoublyLinkedNode<T> | null,
    value: T
}

export class DoublyLinkedList<T> {
    private _head: DoublyLinkedNode<T> | null
    private _tail: DoublyLinkedNode<T> | null

    public static from<U>(values: U[]): DoublyLinkedList<U> {
        const linkedList = new DoublyLinkedList<U>()

        for (const value of values) {
            linkedList.pushBack(value)
        }

        return linkedList
    }

    public constructor() {
        this._head = null
        this._tail = null
    }

    public get head(): DoublyLinkedNode<T> | null {
        return this._head
    }

    public get tail(): DoublyLinkedNode<T> | null {
        return this._tail
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

    public pushFront(value: T): void {
        const newHead: DoublyLinkedNode<T> = { next: this._head, prev: null, value }

        if (this.isEmpty) {
            this._tail = newHead
        } else {
            this._head!.prev = newHead
        }

        this._head = newHead
    }

    public popBack(): T | undefined {
        if (this.isEmpty) {
            return undefined
        }

        const value = this._tail!.value

        if (this._head === this._tail) {
            this._head = null
            this._tail = null

        } else {
            const newTail = this._tail!.prev!

            newTail.next = null
            this._tail = newTail
        }

        return value
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

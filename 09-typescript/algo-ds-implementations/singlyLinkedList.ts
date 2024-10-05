export interface SinglyLinkedNode<T> {
    next: SinglyLinkedNode<T> | null,
    value: T
}

export class SinglyLinkedList<T> {
    private _head: SinglyLinkedNode<T> | null
    private _tail: SinglyLinkedNode<T> | null

    public static from<U>(values: U[]): SinglyLinkedList<U> {
        const linkedList = new SinglyLinkedList<U>()

        for (const value of values) {
            linkedList.pushBack(value)
        }

        return linkedList
    }

    public constructor() {
        this._head = null
        this._tail = null 
    }

    public get head(): SinglyLinkedNode<T> | null {
        return this._head
    }

    public get tail(): SinglyLinkedNode<T> | null {
        return this._tail
    }

    public get isEmpty(): boolean {
        return this._head === null
    }

    public pushFront(value: T): void {
        const newHead = { value, next: this._head }

        if (this.isEmpty) {          
            this._tail = newHead
        }

        this._head = newHead
        
    }

    public pushBack(value: T): void {
        const newTail = { value, next: null }

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
            this._head = this.head!.next
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
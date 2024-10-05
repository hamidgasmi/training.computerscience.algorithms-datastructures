export class Stack<T> {
    private readonly stack: T[]

    public constructor() {
        this.stack = []
    }

    public push(value: T): void {
        this.stack.push(value)
    }

    public pop(): T | undefined {
        return this.stack.pop()
    }

    public get size(): number { 
        return this.stack.length 
    }

    public toString(): string {
        return this.stack.join(',')
    }
}
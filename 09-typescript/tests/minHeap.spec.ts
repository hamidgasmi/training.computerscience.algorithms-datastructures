import { expect } from 'chai'
import itParam from 'mocha-param'
import { MinHeap } from '../problems/commonDataStructures/minHeap'

describe('MinHeap Unit Test', function () {
    const array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    const priorityQueue = [0,1,4,2,6,5,8,3,7,9,10]
    let heapQueue: MinHeap<number>

    beforeEach(() => {
        heapQueue = MinHeap.build(array)
    })

    describe('build', function () {
        itParam('should be successfull when input is empty', [[], undefined], (arr: undefined | number[]) => {
            heapQueue = MinHeap.build(arr)

            expect(heapQueue.size).to.equal(0)
            expect(heapQueue.getMin()).to.equal(undefined)
            expect(heapQueue.extractMin()).to.equal(undefined)
            expect(heapQueue.toString()).to.equal('')

            heapQueue.insert(0)
            expect(heapQueue.getMin()).to.equal(0)
            expect(heapQueue.size).to.equal(1)
            expect(heapQueue.toString()).to.equal('0')
        })

        it('should be successfull when minHeap has 1 element', () => {
            heapQueue = MinHeap.build([1])

            expect(heapQueue.getMin()).to.equal(1)
            expect(heapQueue.size).to.equal(1)
            expect(heapQueue.toString()).to.equal('1')

            expect(heapQueue.extractMin()).to.equal(1)
            expect(heapQueue.getMin()).to.equal(undefined)
            expect(heapQueue.size).to.equal(0)
            expect(heapQueue.toString()).to.equal('')

            heapQueue.insert(1)
            expect(heapQueue.getMin()).to.equal(1)
            expect(heapQueue.size).to.equal(1)
            expect(heapQueue.toString()).to.equal('1')

            heapQueue.insert(2)
            expect(heapQueue.getMin()).to.equal(1)
            expect(heapQueue.size).to.equal(2)
            expect(heapQueue.toString()).to.equal('1,2')

            heapQueue.insert(0)
            expect(heapQueue.getMin()).to.equal(0)
            expect(heapQueue.size).to.equal(3)
            expect(heapQueue.toString()).to.equal('0,2,1')
        })

        it('should be successfull when input has 2 elements', () => {
            heapQueue = MinHeap.build([1,2])

            expect(heapQueue.getMin()).to.equal(1)
            expect(heapQueue.size).to.equal(2)
            expect(heapQueue.toString()).to.equal('1,2')
            expect(heapQueue.extractMin()).to.equal(1)

            expect(heapQueue.getMin()).to.equal(2)
            expect(heapQueue.size).to.equal(1)
            expect(heapQueue.toString()).to.equal('2')
        })

        it('should be successfull when input has values', () => {
            expect(heapQueue.size).to.equal(array.length)
            expect(heapQueue.getMin()).to.equal(0)
            expect(heapQueue.toString()).to.equal(priorityQueue.join(','))

            heapQueue.insert(11)
            expect(heapQueue.getMin()).to.equal(0)
            expect(heapQueue.size).to.equal(priorityQueue.length + 1)
            expect(heapQueue.toString()).to.equal([...priorityQueue, 11].join(','))

            heapQueue.insert(-1)
            expect(heapQueue.getMin()).to.equal(-1)
            expect(heapQueue.size).to.equal(priorityQueue.length + 2)
            expect(heapQueue.toString()).to.equal(`-1,1,0,2,6,4,8,3,7,9,10,11,5`)

            for(let i = -1; i < array.length + 1; i++) {
                expect(heapQueue.size).to.equal(priorityQueue.length - i + 1)
                expect(heapQueue.getMin()).to.equal(i)
                expect(heapQueue.extractMin()).to.equal(i)
            }
        })
    })

    describe('getLeft', function () {
        itParam('should return -1 when left child does not exist', [-1, 5, 6 ], (i: number) => {
            expect(heapQueue.getLeft(i)).to.equal(-1)
        })

        itParam('should return -1 when left child does not exist', [0, 1, 2, 3, 4 ], (i: number) => {
            expect(heapQueue.getLeft(i)).to.equal(2 * i + 1)
        })
    })

    describe('getRight', function () {
        itParam('should return -1 when left child does not exist', [-1, 5, 6 ], (i: number) => {
            expect(heapQueue.getRight(i)).to.equal(-1)
        })

        itParam('should return -1 when right child does not exist', [0, 1, 2, 3, 4 ], (i: number) => {
            expect(heapQueue.getRight(i)).to.equal(2 * i + 2)
        })
    })

    describe('getParent', function () {
        itParam('should return -1 when parent child does not exist', [-1, 0, 11 ], (i: number) => {
            expect(heapQueue.getParent(i)).to.equal(-1)
        })

        itParam('should return -1 when left child does not exist', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], (i: number) => {
            expect(heapQueue.getParent(i)).to.equal(Math.floor((i - 1) / 2))
        })
    })

    describe('getElement', function () {
        itParam('should return undefined when element does not exist', [-1, 11 ], (i: number) => {
            expect(heapQueue.getElement(i)).to.equal(undefined)
        })

        itParam('should return correct element when it exists', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], (i: number) => {
            expect(heapQueue.getElement(i)).to.equal(priorityQueue[i])
        })
    })

    describe('siftDown', function () {
        itParam('should not do any when index is invalid', [-1, 11 ], (i: number) => {
            expect(heapQueue.siftDown(i)).to.equal(undefined)
        })
    })

    describe('siftUp', function () {
        itParam('should not do any when index is invalid', [-1, 11 ], (i: number) => {
            expect(heapQueue.siftUp(i)).to.equal(undefined)
        })
    })
})

import { expect } from 'chai'
import itParam from 'mocha-param'
import { DoublyLinkedList, DoublyLinkedNode } from '../problems/commonDataStructures/doublyLinkedList'

describe('DoublyLinkedList Unit Test', function () {
    let linkedList: DoublyLinkedList<number>
    const randomValues = [ Math.random() * 10, Math.random() * 10, Math.random() * 10]

    beforeEach(() => {
        linkedList = new DoublyLinkedList<number>()
    })
    
    itParam('DoublyLinkedList.from should be successfull when ${value.description}', [
        { description: 'input array is empty', values: [], isEmpty: true },
        { description: 'input array has one element', values: [ randomValues[0] ] },
        { description: 'input array has multiple elements', values: [ ...randomValues ] }
    ], ({ values }: { description: string, values: number[] }) => {
        linkedList = DoublyLinkedList.from<number>(values)

        expect(linkedList.isEmpty).to.equal(!values.length)
        expect(linkedList.toString()).to.equal(values.join(','))

        let lrNode = linkedList.head
        let rlNode = linkedList.tail
        for (let i = 0; i < values.length; i++) {
            expect(lrNode!.value).to.equal(values[i])
            expect(rlNode!.value).to.equal(values[values.length - i - 1])

            lrNode = lrNode!.next
            rlNode = rlNode!.prev
        }
        expect(lrNode).to.equal(null)
        expect(rlNode).to.equal(null)
    })

    it('Operations should be successfull when linked-list is empty', () => {
        expect(linkedList.isEmpty).to.equal(true)
        expect(linkedList.head).to.equal(null)
        expect(linkedList.head).to.equal(linkedList.tail)
        expect(linkedList.popFront()).to.equal(undefined)
        expect(linkedList.popBack()).to.equal(undefined)
        expect(linkedList.toString()).to.equal('')
    })

    describe('pushBack', function () {
        it('should be successfull when linked-list is empty', () => {
            linkedList.pushBack(randomValues[0])
    
            expect(linkedList.isEmpty).to.equal(false)
            expect(linkedList.head).to.deep.eq({ next: null, prev: null, value: randomValues[0] })
            expect(linkedList.head).to.equal(linkedList.tail)
            expect(linkedList.toString()).to.equal(`${randomValues[0]}`)
        })

        it('should be successfull when linked-list is not empty', () => {
            randomValues.forEach(value => linkedList.pushBack(value))

            expect(linkedList.isEmpty).to.equal(false)

            let lrNode = linkedList.head
            let rlNode = linkedList.tail
            for (let i = 0; i < randomValues.length; i++) {
                expect(lrNode!.value).to.equal(randomValues[i])
                expect(rlNode!.value).to.equal(randomValues[randomValues.length - i - 1])

                lrNode = lrNode!.next
                rlNode = rlNode!.prev
            }
            expect(lrNode).to.equal(null)
            expect(rlNode).to.equal(null)

            expect(linkedList.toString()).to.equal(randomValues.join(','))
        })
    })

    describe('pushFront', function () {
        it('should be successfull when linked-list is empty', () => {
            linkedList.pushFront(randomValues[0])
    
            expect(linkedList.isEmpty).to.equal(false)
            expect(linkedList.head).to.deep.eq({ next: null, prev: null, value: randomValues[0] })
            expect(linkedList.head).to.equal(linkedList.tail)
            expect(linkedList.toString()).to.equal(`${randomValues[0]}`)
        })

        it('should be successfull when linked-list is not empty', () => {
            randomValues.forEach(value => linkedList.pushFront(value))

            expect(linkedList.isEmpty).to.equal(false)

            let lrNode = linkedList.head
            let rlNode = linkedList.tail
            for (let i = 0; i < randomValues.length; i++) {
                expect(lrNode!.value).to.equal(randomValues[randomValues.length - i - 1])
                expect(rlNode!.value).to.equal(randomValues[i])

                lrNode = lrNode!.next
                rlNode = rlNode!.prev
            }
            expect(lrNode).to.equal(null)
            expect(rlNode).to.equal(null)

            expect(linkedList.toString()).to.equal([...randomValues].reverse().join(','))
        })
    })

    it('popBack should be successfull when linked-list has multiple element', () => {
        linkedList = DoublyLinkedList.from(randomValues)

        expect(linkedList.isEmpty).to.equal(false)

        let rlNode = linkedList.tail

        for (let i = randomValues.length - 1; i > -1; i--) {
            expect(linkedList.tail).to.equal(rlNode)
            expect(linkedList.popBack()).to.equal(randomValues[i])
            if (!linkedList.isEmpty) {
                expect(linkedList.tail?.next).to.equal(null)
            }

            rlNode = rlNode!.prev
        }
        expect(rlNode).to.equal(null)
        expect(linkedList.head).to.equal(null)
        expect(linkedList.tail).to.equal(null)

        expect(linkedList.isEmpty).to.equal(true)
    })

    it('popFront should be successfull when linked-list has multiple element', () => {
        linkedList = DoublyLinkedList.from(randomValues)

        expect(linkedList.isEmpty).to.equal(false)

        let lrNode = linkedList.head

        for (const value of randomValues) {
            expect(linkedList.head).to.equal(lrNode)
            expect(linkedList.popFront()).to.equal(value)
            if (!linkedList.isEmpty) {
                expect(linkedList.head?.prev).to.equal(null)
            }

            lrNode = lrNode!.next
        }
        expect(lrNode).to.equal(null)
        expect(linkedList.head).to.equal(null)
        expect(linkedList.tail).to.equal(null)

        expect(linkedList.isEmpty).to.equal(true)
    })
})

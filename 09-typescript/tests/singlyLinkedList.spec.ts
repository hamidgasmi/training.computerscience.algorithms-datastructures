import { expect } from 'chai'
import itParam from 'mocha-param'
import { SinglyLinkedList } from '../problems/commonDataStructures/singlyLinkedList'

describe('SinglyLinkedList Unit Test', function () {
    let linkedList: SinglyLinkedList<number>
    const randomValues = [ Math.random() * 10, Math.random() * 10, Math.random() * 10]

    beforeEach(() => {
        linkedList = new SinglyLinkedList<number>()
    })
    
    itParam('SinglyLinkedList.from should be successfull when ${value.description}', [
        { description: 'input array is empty', values: [], isEmpty: true },
        { description: 'input array has one element', values: [ randomValues[0] ] },
        { description: 'input array has multiple elements', values: [ ...randomValues ] }
    ], ({ values }: { description: string, values: number[] }) => {
        linkedList = SinglyLinkedList.from(values)

        expect(linkedList.isEmpty).to.equal(!values.length)
        expect(linkedList.toString()).to.equal(values.join(','))

        let node = linkedList.head

        for(const value of values) {
            expect(node!.value).to.equal(value)

            node = node!.next
        }
    })

    it('Operations should be successfull when linked-list is empty', () => {
        expect(linkedList.head).to.equal(null)
        expect(linkedList.head).to.equal(linkedList.tail)
        expect(linkedList.isEmpty).to.equal(true)
        expect(linkedList.toString()).to.equal('')
        expect(linkedList.popFront()).to.equal(undefined)
    })

    describe('pushBack', function () {
        it('should be successfull when linked-list is empty', () => {
            linkedList.pushBack(randomValues[0])
    
            expect(linkedList.isEmpty).to.equal(false)
            expect(linkedList.head).to.deep.eq({ next: null, value: randomValues[0] })
            expect(linkedList.head).to.equal(linkedList.tail)
            expect(linkedList.toString()).to.equal(`${randomValues[0]}`)
        })

        it('should be successfull when linked-list is not empty', () => {
            randomValues.forEach(value => linkedList.pushBack(value))

            expect(linkedList.isEmpty).to.equal(false)

            let node = linkedList.head

            expect(node!.next).to.not.equal(null)
            for(const value of randomValues) {
                expect(node!.value).to.equal(value)
                
                node = node!.next
            }
            expect(node).to.equal(null)
            expect(linkedList.tail!.next).to.equal(null)

            expect(linkedList.toString()).to.equal(randomValues.join(','))
        })
    })

    describe('pushFront', function () {
        it('should be successfull when linked-list is empty', () => {
            linkedList.pushFront(randomValues[0])
    
            expect(linkedList.isEmpty).to.equal(false)
            expect(linkedList.head).to.deep.eq({ next: null, value: randomValues[0] })
            expect(linkedList.head).to.equal(linkedList.tail)
            expect(linkedList.toString()).to.equal(`${randomValues[0]}`)
        })

        it('should be successfull when linked-list is not empty', () => {
            randomValues.forEach(value => linkedList.pushFront(value))

            expect(linkedList.isEmpty).to.equal(false)

            let node = linkedList.head
            const reversedRandomValues = [ ...randomValues ].reverse()

            expect(node!.next).to.not.equal(null)
            for(const value of reversedRandomValues) {
                expect(node!.value).to.equal(value)
                
                node = node!.next
            }
            expect(node).to.equal(null)
            expect(linkedList.tail!.next).to.equal(null)

            expect(linkedList.toString()).to.equal(reversedRandomValues.join(','))
        })
    })

    it('popFront should be successfull when linked-list has multiple element', () => {
        linkedList = SinglyLinkedList.from(randomValues)

        expect(linkedList.isEmpty).to.equal(false)

        let node = linkedList.head

        for (const value of randomValues) {
            expect(linkedList.head).to.equal(node)
            expect(linkedList.popFront()).to.equal(value)

            node = node!.next
        }

        expect(linkedList.isEmpty).to.equal(true)
    })
})

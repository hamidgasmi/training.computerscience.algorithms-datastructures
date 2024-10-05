import { expect } from 'chai'
import { Queue } from '../problems/commonDataStructures/queue'

describe('Queue Unit Test', function () {
    let queue: Queue<number>
    const randomValues = [ Math.random() * 10, Math.random() * 10, Math.random() * 10]

    beforeEach(() => {
        queue = new Queue<number>()
    })

    it('Operations should be successfull when stack is empty', () => {
        expect(queue.size).to.equal(0)
        expect(queue.deQueue()).to.equal(undefined)
        expect(queue.toString()).to.equal('')
    })

    it('Operations should be successfull when stack has 1 element', () => {
        queue.enQueue(randomValues[0])

        expect(queue.size).to.equal(1)
        expect(queue.toString()).to.equal(`${randomValues[0]}`)
        expect(queue.deQueue()).to.equal(randomValues[0])
    })

    it('Operations should be successfull when stack has multiple elements', () => {
        randomValues.forEach(value => queue.enQueue(value))

        expect(queue.size).to.equal(randomValues.length)
        expect(queue.toString()).to.equal(randomValues.join(','))

        for(let i = 0; i < randomValues.length; i++) {
            expect(queue.deQueue()).to.equal(randomValues[i])
            expect(queue.size).to.equal(randomValues.length - i - 1)
            expect(queue.toString()).to.equal(randomValues.slice(i + 1, randomValues.length).join(','))
        }
    })
})

import { expect } from 'chai'
import { Stack } from '../problems/commonDataStructures/stack'

describe('Stack Unit Test', function () {
    let stack: Stack<number>
    const randomValues = [ Math.random() * 10, Math.random() * 10, Math.random() * 10]

    beforeEach(() => {
        stack = new Stack()
    })

    it('Operations should be successfull when stack is empty', () => {
        expect(stack.size).to.equal(0)
        expect(stack.pop()).to.equal(undefined)
        expect(stack.toString()).to.equal('')
    })

    it('Operations should be successfull when stack has 1 element', () => {
        stack.push(randomValues[0])
        expect(stack.size).to.equal(1)
        expect(stack.toString()).to.equal(`${randomValues[0]}`)
        expect(stack.pop()).to.equal(randomValues[0])
    })

    it('Operations should be successfull when stack has multiple elements', () => {
        randomValues.forEach(value => stack.push(value))
        expect(stack.size).to.equal(randomValues.length)
        expect(stack.toString()).to.equal(randomValues.join(','))

        for(let i = 0; i < randomValues.length; i++) {
            expect(stack.pop()).to.equal(randomValues[ randomValues.length - i - 1])
            expect(stack.size).to.equal(randomValues.length - i - 1)
            expect(stack.toString()).to.equal(randomValues.slice(0, randomValues.length - i - 1).join(','))
        }
    })
})

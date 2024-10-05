import { expect } from 'chai'
import itParam from 'mocha-param'
import { sumImbalanceNumbers } from './sumImbalanceNumbers'

describe('sumImbalanceNumbers Unit Test', function () {
    itParam('For input ${value.input} should return ${value.expectedOutput}', [
        { input: [1,1,1], expectedOutput: 0 },
        { input: [1,2,3], expectedOutput: 0 },
        { input: [2,3,1,4], expectedOutput: 3 },
        { input: [1,4,4,1], expectedOutput: 5 },
        { input: [1,3,3,3,5], expectedOutput: 8 },
        { input: [1,5,3,2,4], expectedOutput: 7 },
        { input: [3,5,2,5,1], expectedOutput: 10 }
    ], ({ input, expectedOutput }: { input: number[], expectedOutput: number }) => {
        expect(sumImbalanceNumbers(input)).to.equal(expectedOutput)
    })
})

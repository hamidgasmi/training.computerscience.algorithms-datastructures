import { expect } from 'chai'
import itParam from 'mocha-param'
import { productExceptSelf } from './productOfArrayExceptSelf'

describe('productExceptSelf Unit Test', function () {
    itParam('For input ${value.input} should return ${value.expectedOutput}', [
        { input: [1,2], expectedOutput: [2,1] },
        { input: [1,2,3], expectedOutput: [6,3,2] },
        { input: [1,2,3,4], expectedOutput: [24,12,8,6] },
        { input: [1,0,3,4], expectedOutput: [0,12,0,0] },
        { input: [1,-2,3,-4], expectedOutput: [24,-12,8,-6] },
        { input: [1,-2,3,4], expectedOutput: [-24,12,-8,-6] }
    ], ({ input, expectedOutput }: { input: number[], expectedOutput: number[] }) => {
        expect(productExceptSelf(input)).to.deep.eq(expectedOutput)
    })
})

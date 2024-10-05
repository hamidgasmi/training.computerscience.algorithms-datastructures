import { expect } from 'chai'
import itParam from 'mocha-param'
import { fizzBuzz } from './fizzBuzz'

describe('FizzBuzz Unit Test', function () {
    itParam('For input ${value.n} should return ${value.expectedOutput}', [
        { n: 0, expectedOutput: [] },
        { n: 1, expectedOutput: ['1'] },
        { n: 16, expectedOutput: ['1','2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16'] }
    ], ({ n, expectedOutput }: { n: number, expectedOutput: string[] }) => {
        expect(fizzBuzz(n)).to.deep.eq(expectedOutput)
    })
})

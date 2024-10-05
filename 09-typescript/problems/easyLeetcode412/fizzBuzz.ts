export function fizzBuzz(n: number): string[] {
    const answer: string[] = []

    for (let i = 1; i <= n; i++) {
        answer.push(getFizzBuzz(i))
    }

    return answer
}

function getFizzBuzz(i: number): string {
    const isMultipleOf3 = isMultipleOf(i, 3)
    const isMultipleOf5 = isMultipleOf(i, 5)

    if (isMultipleOf3 && isMultipleOf5) {
        return 'FizzBuzz'
    } else if (isMultipleOf3) {
        return 'Fizz'
    } else if (isMultipleOf5) {
        return 'Buzz'
    } else {
        return i.toString()
    }
}

function isMultipleOf(i: number, m: number): boolean {
    return i % m ? false : true
}

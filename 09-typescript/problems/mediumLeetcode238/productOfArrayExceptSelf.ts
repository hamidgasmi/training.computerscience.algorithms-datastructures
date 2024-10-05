export function productExceptSelf(nums: number[]): number[] {

    const productExceptSelf: number[] = [1]

    let leftProduct = 1
    for(let i = 1; i < nums.length; i++) {
        leftProduct *= nums[i - 1]
        productExceptSelf.push(leftProduct)
    }

    let rightProduct = 1
    for(let i = nums.length - 2; i > -1; i--) {
        rightProduct *= nums[i + 1]
        productExceptSelf[i] *= rightProduct
    }

    return productExceptSelf
}
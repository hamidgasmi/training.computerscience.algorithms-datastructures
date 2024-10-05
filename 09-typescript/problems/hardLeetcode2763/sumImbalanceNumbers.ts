/*
    1. Problem Summary / Clarifications / TDD:
        Array: [2,3,1,4]
        Sub-Arrays -    Sorted Array    - Imbalance
            2,3:            2,3               0
            2,3,1           1,2,3             0
            2,3,1,4         1,2,3,4           0
            3,1             1,3               1
            3,1,4           1,3,4             1
            1,4             1,4               1
        --------------------------------------------
          Sum                                 3

    2. Intuition:
        - Naive: too slow
        - We could do better:
            - Use sets
            - Array: [2,3,1,4]
                - Sub-array [2]:        Set: [2],       Imbalance: +0
                - Sub-array [2,3]:      Set: [2,3],     Imbalance: +0
                - Sub-array [2,3,1]:    Set: [2,3,1],   Imbalance: +0
                - Sub-array [2,3,1,4]:  Set: [2,3,1,4], Imbalance: +0
            - Array: [3,1,4]
                - Sub-array [3]:        Set: [3],       Imbalance: +0
                - Sub-array [3,1]:      Set: [3,1]      Imbalance: +1
                - Sub-array [3,1,4]:    Set: [3,1,4],   Imbalance: +1
            - Array: [1,4]
                - Sub-array [1]         Set: [1]        Imbalance: +0
                - Sub-array [1,4]       Set: [1,4]      Imbalance: +1

    3. Implementation
    4. Tests:
    5. Complexity Analysis:
       Time Complexity: O(n^2)
       Space Compexity: O(n)
*/


export function sumImbalanceNumbers(nums: number[]): number {
    let sumImbalanceNumber = 0

    for(let i = 0; i < nums.length; i++) {
        const seenNumbers = new Set([nums[i]])
        
        let currMin = nums[i]
        let currMax = nums[i]
        let distinctGroupsCount = 1

        for (let j = i + 1; j < nums.length; j++) {
            const jnum = nums[j]

            if (!seenNumbers.has(jnum)) {
                if ((jnum < currMin - 1) || (jnum > currMax + 1)) {
                    distinctGroupsCount += 1

                } else if (jnum > currMin && jnum < currMax && !seenNumbers.has(jnum - 1) && !seenNumbers.has(jnum + 1)) {
                    distinctGroupsCount += 1

                } else if (seenNumbers.has(jnum - 1) && seenNumbers.has(jnum + 1)) {
                    distinctGroupsCount -= 1
                }
            }

            seenNumbers.add(jnum)
            currMin = currMin > jnum ? jnum : currMin
            currMax = currMax < jnum ? jnum : currMax

            sumImbalanceNumber += (distinctGroupsCount - 1)
        }
    }

    return sumImbalanceNumber
}

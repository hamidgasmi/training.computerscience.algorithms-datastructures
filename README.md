# Algorithms and Data Structures

- My notes from UC San Diego MicroMasters Program, [Algorithms and Data Structures](https://www.edx.org/micromasters/ucsandiegox-algorithms-and-data-structures)
- My anki flashcards:
    - [Anki flashcards package](https://github.com/hamidgasmi/AlgorithmsDataStructures/blob/master/algorithms-datastructures_ankiflashcard.apkg): 9 cards
    - [Install Anki](https://apps.ankiweb.net/)

## Table of Contents
- [Algorithm Design and Techniques](#algorithm-design-and-techniques)
- [Data Structures Fundamentals](#data-structures-fundamentals)
- [Graph Algorithms](#graph-algorithms)
- [NP-Complete Problem](#np-complete-problem)
- [String Processing and Pattern Matching Algorithms](#string-processing-and-pattern-matching-algorithms)
- [Dynamic Programming: Applications In Machine Learning and Genomics](#dynamic-programming-applications-in-machine-learning-and-genomics)
- [Graph Algorithms in Genome Sequencing ](#graph-algorithms-in-genome-sequencing)
- [Algorithms and Data Structures Capstone](#algorithms-and-data-structures-capstone)

## Algorithm Design and Techniques

<details>
<summary>Prerequisites</summary>

- **Proof by Induction**
    - It allows to prove a statement about an arbitrary number n by:
        - 1st proving it's true when n is 1 and then 
        - assuming it's true for n = k and showing it's true for n = k + 1
    - [For more details](http://comet.lehman.cuny.edu/sormani/teaching/induction.html)
- **Proofs  by contradiction**
    - It allow to prove a proposition is valid (true) by showing that assuming the proposition to be false leads to a contradiction
    - [For more details](https://en.wikipedia.org/wiki/Proof_by_contradiction)
- **T(n)** is the number of lines of code executed by an algorithm
- **Logarithms**: see [this](https://www.khanalscademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:log-intro/a/intro-to-logarithms)
- **Recursion**: 
    - To [Get Started](https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursion)
    - Stack optimization and Tail Recursion

</details>

<details>
<summary>Test Cases</summary>

- **Boundary** values
- **Biased**/**Degenerate** tests cases
    - They're tests which are peculiar in some sense
    - See example for each data structure below
- **Randomly** generated cases and **large** dataset:
    - It's to check random values to catch up cases we didn't think about
    - It's also to check how long it takes to process a large dataset
    - Implement our program as a function **solve(dataset)**
    - Implement an additional procedure **generate()** that produces a random/large dataset 
    - E.g., if an input to a problem is a sequence of integers of length 1 ≤ n ≤ 10^5, then: 
        - Generate a sequence of length 10^5, 
        - Pass it to our solve() function, and 
        - Ensure our algorithm outputs the result quickly: we could measure the duration time
- **Stress** testing:
    - Implement a slow but but simple and correct algorithm
    - Check that both programs produce the same result (this is not applicable to problems where the output is not unique) 
    - Generate random test cases as well as biased tests cases
- When dealing with **numbers**:
    - Think about number size: Int. Long, ... ?
    - If there is any division: division by 0; Precision?
    - Integers Biased cases: a **Prime/Composite** number; an **Even/Odd** number
- When dealing with **String**:
    - Biased/Degenerate tests: 
        - Empty string
        - A strings that contains a  sequence of a single letter (“aaaaaaa”) or 2 letters ("abbaabaa") as opposed to those composed of all possible Latin letters
    - Encoding (ASCII, UTF-8, UTF-16)?
    - Special characters
    - such as those with only small numbers or a small range of large numbers, 
- When dealing with **arrays/lists**:
    - Biased/Degenerate tests: 
        - It's empty
        - It contains only small numbers or a small range of large numbers
    - It contains **few** elements: 1, 2
    - It contains **many** elements: 10^6
    - It contains same elements: min value only (0 for integers), max value only (2^32 for integers), any specific value
- When dealing with **Trees**:
    -  Biased/Degenerate tests: a tree which consists of a linked list, binary trees, stars
- When dealing with **Graphs**:
    -  Biased/Degenerate tests: a graph which consists of a linked list, a tree, a disconnected graph, a complete graph, a bipartite graph

</details>

<details>
<summary>Big O vs. Big-Ω vs. Big-Θ</summary>

- **Big-Ω** (Omega):
    - It's a lower bound of a function
    - A function f(n) = Ω(g(n)), if there're positive constants C and k, such that 0 ≤ C g(n) ≤ f(n) for all n ≥ k
    - E.g., f(n) = n^2 + n = Ω(n) because n ≤ f(n) for n ≥ 1
    - ![Example](https://xlinux.nist.gov/dads/Images/omegaGraph.gif)
    - It's NOT used in the industry
- **Big-O**:
    - It's an upper bound of a function
    - A function f(n) = O(g(n)), if there're positive constants C and k, such that 0 ≤ f(n) ≤ C g(n) for all n ≥ k
    - E.g., f(n) = n^2 = O(n^3) because f(n) ≤ n^3 for k ≥ 1
    - ![Example](https://upload.wikimedia.org/wikipedia/commons/8/89/Big-O-notation.png)
    - It's used in the Industry with a different definition (see below, Big-Theta)
- **Big-Θ** (Theta):
    - A function f grows at same rate as a function g
    - If f = Ω(g) and f = O(g)
    - E.g., f(n) = n^2 + n = Θ(n^2) because n^2 ≤ f(n) ≤ n^2 for k ≥ 1
    - It's used in the industry as Big-O
- **Small-o**:
    - A function f is o(g) if f(n)/g(n) → 0 as n → ∞
    - f grows slower than g
    - It's NOT used in the industry
- [For more details](https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/asymptotic-notation)

</details>

<details>
<summary>Time Complexity</summary>

- It describes the rate of increase of an algorithm
- It describes how an algorithm scales when input grows
- Big-O notation is used
- It's also called **Asymptotic runtime**:
    - It's only asymptotic
    - It tells us about what happens when we put really big inputs into the algorithm
    - It doesn't tell us anything about how long it takes
    - Its hidden constants:
        - They're usually moderately small, and therefore, we have something useful
        - They're could be big
    - Sometimes an algorithm A with worse Big-O runtime than algorithm B:
        - Algorithm A is worse asymptotically on very large inputs than algorithm B does
        - But algorithm A is better for all practical sizes and very large inputs couldn't be stored 
- E.g., O(1), O(n), O(n^2) , O(Log n), O(n log n), O(2^n)
- [Data structure and theirs related algorithms time complexity](https://www.bigocheatsheet.com/)

</details>

<details>
<summary>Space Complexity</summary>

- It describes the amount of memory - or space - required for an algorithm
- It useful to compare the performance of algorithms
    - Input size from which an algorithm will experience unsufficient memory (RAM) and start using Disk lookups
- Big O notation and concept are used 

</details>

<details>
<summary>Big-O Rules</summary>

- **Drop the constants**: we'll use O(n) instead of O(2 n)
- **Drop the Non-Dominant Terms**: we'll use O(n^2) instead of O(n^2 + n) or O(n) instead of O(n + log n) 
- Multi-Part Algorithms - Add: **O(A+B)**
    - When an algorithm  is in the form 
    - Do A, 
    - When you're done, Do B
- Multi-Part Algorithms - Multiply: **O(A*B)**
    - When an algorithm is in the form: 
    - Do B for each time you do A
- **Amortized Time**
    - When the worst case happens once a while 
    - But once it happens, it won't happen again for so long that the cost is "amortized" 
    - E.g., insert in a dynamic resizing array (an array list): 
        - It's implemented with an array 
        - When the array hits its capacity, it will create a new array with double the capacity and copy all the elements over to the new array
        - Insert time complexity in expected case (the array isn't full): O(1)
        - Insert time complexity in worst case (the array is full): O(n)
        - Insert time complexity for n inserts: O(n) (for n expected cases) + O(w * n) (w worst cases): O((w+1)n) = O(n)
        - The amortization time for each insertion (the time complexity for n inserts divided by n): O(1)
- **Log n** runtimes: O(log n)
    - It when the number of elements in a problem space is halved each time (or divided by n) 
    - E.g. **Dichotomic search**: search in a sorted array
- The base of Log(n) isn't import
    - E.g. O(Log2 n) = O(Log3 n) = O(Log n) 
- **Recursive Runtimes**, a recursive algorithm usually is defined by:
    - Its **depth**: n and the **number of times each recursive call branches** (itself). 
    - **Time complexity: O(branchesNbr^n)** 
    - **Space complexity: O(n)**
    - E.g., Fibonacci Recursive time complexity: O(2^n)
    - E.g., Fibonacci Space complexity: O(n): because only O(N) nodes exist at any given time 
- The **base of an Exponent**:
    - Log(8^n) is completely different than Log(2^n)
 
</details>

<details>
<summary>Algorithm Design</summary>

- **Reading problem statement**: 
    - The problem statement specifies the input-output format, the constraints for the input data as well as time and memory limits 
    - Our goal is to implement a fast program that solves the problem and works within the time and memory limits
    - Question inputs:
        - **String**: Encoding (ASCII, UTF-8, UTF-16)?, Special characters?
        - **Number**: Size (Int. Long, ...)? Precision, Rounding?
- **Build your intuition**:
    - *In progress*
- **Designing an algorithm**: 
    - When the problem statement is clear, start designing an algorithm and 
    - Don’t forget to **prove that it works correctly**
    - Don't forget to **estimate its expected running time**:
        - E.g.
        -       Time Complexity:     O(n^2)                  O(n log n)
                    Machine ops:      10^9                   10^9
                              n:      10^5                   10^5
                 Estimated Time:      > 10s (10^10/10^9)     < 1 ms (10^5*log(10^5)/10^9)
- **Implementing an algorithm**: 
    - After you developed an algorithm, start implementing it in a programming language
- **Testing and debugging your program** 
    - Testing is the art of revealing bugs
    - 1st start with **simple test cases**: 
        - Small dataset
        - Make sure our program produces correct results
    - 2nd check **degenerate** cases: see test cases section above
    - 3rd check **boundary** values: see test cases section above
    - 4th check **randomly** generated cases
    - 5th check **large** dataset: see test cases section above
    - 6th finish with **stress** testing: see test cases section above

</details>

<details>
<summary>General Approaches</summary>

- **Tournament** approach:
    - To find the kth largest number in an array, compare each paire of 2 elements together
    - compare(elem 0, elem 1), compare(elem 2, elem 3)...
    - O(n + log(n) − 2)
- **Euclidean** Algorithm

</details>

<details>
<summary>Greedy Algorithms</summary>

- **Greedy Strategy**:
    - **1. Make a greedy choice**
    - **2. Prove that it is a safe choice**
    - **3. Reduce to a subproblem**
    - **4. Solve the subproblem (Iterate)**
    - E.g. Problem, Queue of Patients:
        - n patients have come to the doctor’s office at same time
        - Ti is the time needed for treatment of the i-th patient
        - They can be treated in any order 
        - Output: Arrange the patients in such a queue that the total waiting time is minimized
    - E.g. Solution:
        - Make a greedy choice: choose the patient (Pi) with the smallest treatment time (with the minimum Ti)
        - Prove that it's a safe choice
        - Reduce to a smaller problem: remove Pi from the queue
        - Iterate: Treat all the remaining patients in such order as to minimize their total waiting time as if there wasn't 1st patient
- **Subproblem** 
    - It's a similar problem of smaller size
    - Minimum total waiting time for n patients = (n − 1) · T min + minimum total waiting time for n − 1 patients without T min
    - Min total waiting time for n = 4 partients: (15, 10, 25, 20) = (4 - 1) * 10 + Min total waiting time for (15, 25, 20)
- **Safe Choice**:
    - It's a greedy choice which there's an optimal solution consistent with this 1st choice
    - It requires to **prove** that a greedy choice is safe
    - E.g. Queue of Patients: 
        - If we prove that there's an optimal solution that starts with treating a patient with the minimum treatment time
        - Therefore such a choice is a safe choice
        - However, if we choose a patient with the maximum treatment time, there's not an optimal solution that starts with it
        - Therefore such a choice isn't a safe choice
- E.g. Fractional Knapsack (or Backpack) Problem:
    - N items with total weight and total value (Wi, Vi)    
    - A Backpack with a capacity W
    - Goal: Maximize value ($) while limiting total weight (kg)
    - It's possible to take fraction of items
    - Item 1: (6, $30), Item 2 (3, $14), Item 3 (4, $16), Item 4 (2, $9)
        - Knapsack capacity: 10
        - Value per Unit: Item 1: $5; Item2: $4.66; Item3: $4; Item4: $4.5
        - Solution: 6 * $5 + 3 * $4.666 + 1 * $4.5 (fraction of item4) = $48.5

</details>

<details>
<summary>Divide and Conquer</summary>

- **Divide**: Break into non-overlapping subproblems of the same type
- **Conquer**:
    - Solve subproblems: each one indepently of the others
    - Combine results
- Implementation: it's often implemented with a **recursive** algorithm
- Calculate its Time Complexity:
    - Define a corresponding **recurrence relation**, **T**
        - It's an equation recursively defining a sequence of values
        - For Linear Search *T(n) = T(n - 1) + c*; *T(0) = c*
        - *c* is the runtime for a constant amount of work: checking high vs. low indexes; if A[low] == key); preparing the parameters for the recursive call
        - *T(0)* is the runtime for the **base case** of the recursion (empty array): checking high vs. low indexes, returning not found
        - For Binary Search *T(n) = T(n/2) + c*; *T(0) = c*
    - Determine **worst-case runtime**, T(n) from the recurrence relation
        - Look at the **recursion tree**
        - For Linear Search T(n) = T(n - 1) + c = T(n - 2) + 2 * c = n * c = T(n) = Θ(n)
        - For Binary Search T(n) = T(n/2) + c = T(n/2^2) + 2 * c = T(n/2^3) + 3 * c = Θ(log2 n) = Θ(log n)
- Optionally, create iterative solution
    - It allows to save space
- For more details:
    - [Binary Search](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)
    - **Merge Sort**
        - [Course Material](https://github.com/hamidgasmi/algorithms-datastructures/blob/master/1_algorithm_design_and_techniques/week4_divide_and_conquer/03_divide_and_conquer_4_sorting.pdf)
        - [Merge Sort on khanacademy](https://www.khanacademy.org/computing/computer-science/algorithms#merge-sort)
    - **Quick Sort**
        - It's more efficient in practice than Merge Sort
        - Average Time Complexity: O(n log n)
        - Time Complexity in the worst case: O(n^2)
        - [Course Material](https://github.com/hamidgasmi/algorithms-datastructures/blob/master/1_algorithm_design_and_techniques/week4_divide_and_conquer/03_divide_and_conquer_5_quicksort.pdf)
        - [Quick Sort on khanacademy](https://www.khanacademy.org/computing/computer-science/algorithms#quick-sort)
        - [Deterministic and Randomized Quicksort](http://faculty.cs.tamu.edu/klappi/csce411-f12/csce411-set13.pdf)
        - [3 way partition Quick Sort](https://www.geeksforgeeks.org/3-way-quicksort-dutch-national-flag/)
        - [Quick Sort Recursive Tail Elimination](https://www.geeksforgeeks.org/quicksort-tail-call-optimization-reducing-worst-case-space-log-n/)
        - [Quick Sort wth deterministic pivot selection heuristic]:
            - The pivot could be the median of the 1st, middle, and last element
            - If the recursion depth exceeds a certain threshold ***c log n***, the algorithm switches to heap sort
            - It's a simple but heuristic approach:: it's not guaranteed to be optimal
            - The time complexity is: O(n log n) in the worst case
    - [Counting Sort](https://www.geeksforgeeks.org/counting-sort/)

</details>

<details>
<summary>Dynamic Programming</summary>

- It's a general algorithmic design technique: Approach can be used to solve many kinds of problems
- It's Frequently used for optimization problems: finding best way to do something
- It's typically used when brute-force solution is to enumerate all possibilities:
    - May not know which subproblems to solve, so we solve many or all!
    - Reduce number of possibilities by:
        - Finding optimal solutions to subproblems
        - Avoiding non-optimal subproblems (when possible)
        - Frequently gives a polynomial algorithm for brute force exponential one
- It's like Divide and Conquer:
    - General design technique
    - Uses solutions to subproblems to solve larger problems
    - Difference: Dynamic Programming subproblems typically overlap
- It's an alternative for Recursive algorithms:
    - Recursive algorithms may be not efficient: they could do a compute several times
    - E.g. Money change problem MinCoin(40 cents) in Tanzania:
    - MinCoin(40s) = 1 + Min( MinCoin(40c - 1c), MinCoin(40c - 5c), MinCoin(40c - 10c), MinCoin(40c - 20c), MinCoin(40c - 25c))
    - MinCoin(20c) is computed at least 4 times: MinCoin(40c - 1c), MinCoin(40c - 5c), MinCoin(40c - 10c), MinCoin(40c - 20c)
- It's an alternative for Greedy Algorithms: 
    - When there is not a safe choice
    - E.g.1, Money change problem MinCoin(40 cents) in US:
        - US coins <= 40c: 1c, 5c, 10c, 25c
        - A Greedy choice: take the max coin such that coin <= 40c
        - Result: 3 coins: 40c = 1 * 25c + 1 * 10c + 1 * 5c
        - Here this choice is safe
    - E.g.2, Money change problem MinCoin(40 cents) in Tanzania:
        - Tanzanian coins <= 40c: 1c, 5c, 10c, 20c, 25c
        - A greedy choice: take the max coin such that the coin <= 40c
        - Result: 3 coins: 40c = 1 * 25c + 1 * 10c + 1 * 5c
        - Here this choice isn't safe: 40c = 2 * 20c
- Steps:
    - Express a solution mathematically
        - **Cut and Paste Trick Dynamic Programming**:
        - Cut and paste proof: optimal solution to problem must use optimal solution to subproblem: otherwise we could remove suboptimal solution to subproblem and replace it with a better solution, which is a contradiction
        - [For more details](https://stackoverflow.com/questions/9553162/what-is-the-cut-and-paste-proof-technique)
    - Express a solution recursively
    - Either develop a **bottom up algorithm**:
        - Find a bottom up algorithm to find the optimal value
        - Find a bottom up algorithm to construct the solution
    - Or develop a **memoized recursive algorithm**
- **Alignment game** (String Comparison):
    - Remove all symbols from 2 strings in such a way that the number of points is maximized:
    - Remove the 1st symbol from **both** strings: 1 point if the symbols match; 0 if they don't
    - Remove the 1st symbol from **one** of the strings: 0 point
    - E.g.,:    
        -       A T G T T A T A  => A T - G T T A T A
                A T C G T C C    => A T C G T - C - C
                                   +1+1  +1+1         = +4
    - **Sequence Alignment**:
        - It's a 2-row matrix
        - 1st row: symbols of the 1st string (in order) interspersed by "-"
        - 2nd row: symbols of the 2nd string (in order) interspersed by "-"
        - E.g.:  
        -        A T - G T T A T C
                 A T C G T - C - C
                     ^-Del ^--Insert.
        - **Alignment score**: 
            - Premium (**+1**) for every **match** 
            - Penalty (**-μ**) for every **mismatch**
            - Penatly (**-σ**) for every **indel** (insertion/deletion)
            - E.g.:
            -  A T - G T T A T A
               A T C G T - C - C
              +1+1-1+1+1-1-0-1+0 = +1
        - **Optimal alignment**:
            - Input: 2 strings, mismatch penatly μ, and indel penalty σ
            - Output: An alignment of the strings maximizing the score
    - **Common Subsequence**: **Matches** in an alignment of 2 strings form their **common  subsequence**
        - E.g. 
        -      A T - G T T A T C
               A T C G T - C - C
               AT    G T 
              (ATGT) is a common subsequence
- **Longest common subsequence**:
    - Input: 2 strings
    - Output: A longest common subsequence of these strings
    - It corresponds to **highest alignment score** with **μ = σ = 0** (maximizing the score of an alignment)
- **Edit distance**
    - Input: 2 strings
    - Output: the **minimum number of operations** (insertions, deletions, and substitutions of symbols) **to transform one string into another**
    - It corresponds to the **minimum number of mismatches and indels** in an alignment of 2 strings (among all possible alignments)
    - E.g.: 
    -       E D I - T I N G -
            - D I S T A N C E
            ^-Del ^-Ins.----^
    - **Minimizing edit distance = Maximizing Alignment score**
    - Let ***D(i,j)*** be the edit distance of an *i*-prefix *A*[1... *i*] and a *j*-prefix *B*[1.... *j*]
    - ***D(i,j) = MIN(D(i,j-1) + 1, D(i-1,j) + 1, D(i-1,j-1) + 1) if A[i] <> B[j]*** OR
    - ***D(i,j) = MIN(D(i,j-1) + 1, D(i-1,j) + 1, D(i-1,j-1)) if A[i] = B[j]***
- **Reconstructing an **Optimal Alignment**:
    - It could be done by backtracking pointers that are stored in the edit distance computation matrix
- E.g., Discrete Knapsack problem
    - N items with total weight Wi (Kg) and total value Vi ($)
    - A Backpack with a capacity W
    - Each item is either taken or not
    - Goal: Maximize value ($) while limiting total weight (kg)
    - Discrete Knapsack with unlimited repetitions quantities:
        - Input: Weights (W1,..., Wn) and values (V1,..., Vn) of n items; total weight W (Vi’s, Wi’s, and W are non-negative integers)
        - Output: The maximum value of items whose weight doesn't exceed W 
        - Each item can be used any number of times
        - Item 1 (6, $30), Item 2 (3, $14), Item 3 (4, $16), Item 4 (2, $9)
        - Knapsack capacity: 10
        - Solution: 6 ($30) + 2 ($9) + 2 ($9) = $48
        - Greedy Algorithm doesn't work: 6 ($30) + 
    - Discrete Knapsack without one of each repetitions item:
        - Input: Weights (W1,..., Wn) and values (V1,..., Vn) of n items; total weight W (Vi’s, Wi’s, and W are non-negative integers)
        - Output: The maximum value of items whose weight doesn't exceed W 
        - Each item can be used at most once
        - Item 1 (6, $30), Item 2 (3, $14), Item 3 (4, $16), Item 4 (2, $9)
        - Knapsack capacity: 10
        - Solution: 6 ($30) + 4 ($16) = $46
    - Greedy Algorithm fails:
        - Item1 (6, $30), Item2 (3, $14), Item3 (4, $16), Item4 (2, $9)
        - Value per Unit: Item 1: $5; Item2: $4.66; Item3: $4; Item4: $4.5
        - 6 ($30) + 3 ($14) = 9 items ($44)
        - taking an element of maximum value per unit of weight is not safe!
- For more details:
    - [Course material](https://github.com/hamidgasmi/algorithms-datastructures/blob/master/1_algorithm_design_and_techniques/week5_and_6_dynamic_programming/04_dynamic_programming_2_editdistance.pdf)
    - [Advanced dynamic programming lecture notes]() by Jeff Erickson
    - [How Do We Compare Biological Sequences?](https://www.youtube.com/playlist?list=PLQ-85lQlPqFNmbPEsMoxb5dM5qtRaVShn) by Phillip Compeau and Pavel Pevzner
- For more details:
    - [Money change problem: Greedy vs. Recursive vs. Dynamic Programming](https://github.com/hamidgasmi/algorithms-datastructures/blob/master/1_algorithm_design_and_techniques/week5_and_6_dynamic_programming/04_dynamic_programming_1_changeproblem.pdf)
    - [Dynamic Programming](https://www.geeksforgeeks.org/dynamic-programming/) in geeksforgeeks
    - [Dynamic Programming](https://www.radford.edu/~nokie/classes/360/dynprog.html)

</details>

<details>
<summary>Use Cases</summary>

- Fibonacci: calculate number of populations
- GCD: Cryptography, The study of prime numbers in factorization

</details>

---

## Data Structures Fundamentals

<details>
<summary>Basic Data Structures: Arrays</summary>

- It's a contiguous area of memory
- It's consisting of equal-size elements indexed by contiguous integers
- **1-D Array**: accessing **array[i]** consists of accessing the memory address: **array_addr + elem_size × (i − first_index)**
- **2-D Array**:
    - It could be laid out in **Row-Major order**:
        - Its 2nd index (column) changes most rapidly
        - Its elements are laid out as follow: (1,1), (1,2), (1,3), ..., (2,1), (2,2),...
        - Accessing **[i][j]** consists of accessing the memory address: **array_addr + elem_size × [row_lenth * (i  − 1st_row_index) + (j − 1st_column_index)]**
    - It could be laid out in **Column-Major order**:
        - Its 1st index (row) changes most rapidly
        - Its elements are laid out as follow: (1,1), (2,1), (2,1), ..., (1,2), (2,2),...
        - Accessing **[i][j]** consists of accessing the memory address: **array_addr + elem_size × [column_lenth * (j  − 1st_column_index) + (i − 1st_row_index)]**
- Time for common operations:
    -                     Read    Remove   Add
            Beginning:    O(1)     O(n)    O(n) 
                  End:    O(1)     O(1)    O(1)
               Middle:    O(1)     O(n)    O(n)
- Programming Languages:
    - Python: there is no static array data structure

</details>

<details>
<summary>Basic Data Structures: Linked Lists</summary>

- Singly-Linked List
    -                APIs                Time (wout tail)   Time (w tail)         Description 
                PushFront(Key):               O(1)                                 Aadd to front
                Key TopFront():               O(1)                                 Return front item
                    PopFront():               O(1)                                 Remove front item
                 PushBack(Key):               O(n)              O(1)               Add to back
                 Key TopBack():               O(n)              O(1)               Return back item
                     PopBack():               O(n)                                 Remove back item
             Boolean Find(Key):               O(n)                                 Is key in list?
                    Erase(Key):               O(n)                                 Remove key from list
               Boolean Empty():               O(1)                                 Empty list?
          AddBefore(Node, Key):               O(n)                                 Adds key before node
           AddAfter(Node, Key):               O(n)                                 Adds key after node 
- **Doubly-Linked List**:
    - Its node consists of a key, a pointer to the next node and a pointer to the previous node
    -                APIs                    Time (wout tail)   Time (w tail)
                PushFront(Key):               O(1)                                 
                Key TopFront():               O(1)                                 
                    PopFront():               O(1)                                 
                 PushBack(Key):               O(n)              O(1)               
                 Key TopBack():               O(n)              O(1)               
                     PopBack():               O(n)              O(1)                 
             Boolean Find(Key):               O(n)                                 
                    Erase(Key):               O(n)                                 
               Boolean Empty():               O(1)                                 
          AddBefore(Node, Key):               O(n)
           AddAfter(Node, Key):               O(n)
- Programming Languages:
    - Python:

</details>

<details>
<summary>Basic Data Structures: Stacks</summary>

- Programming Languages:
    - Python:

</details>

<details>
<summary>Basic Data Structures: Trees</summary>

- Programming Languages:
    - Python:

</details>

<details>
<summary>Dynamic Arrays</summary>

- Programming Languages:
    - Python: list (the only kind of array)
    - C++: vector
    - Java: ArrayList

</details>

<details>
<summary>Amortized Analysis</summary>

- Methods to calculate amortized cost:
    - The **Aggregate method**: 
        - It calculates amortized cost based on amortized cost definition
        - E.g. Dynamic Array:
    - The **Banker's Method**:
    - The **Physicist's Method**:

</details>

<details>
<summary>Priority Queues and Disjoint Sets</summary>
</details>

<details>
<summary>Hashing</summary>
</details>

<details>
<summary>Binary Search Trees</summary>
</details>

---

## Graph Algorithms

---

## NP-Complete Problem

---

## String Processing and Pattern Matching Algorithms

---

## Dynamic Programming: Applications In Machine Learning and Genomics 

---

## Graph Algorithms in Genome Sequencing

---

## Algorithms and Data Structures Capstone

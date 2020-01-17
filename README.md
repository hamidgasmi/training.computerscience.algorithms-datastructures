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

- **Proof by induction**
    - It allows to prove a statement about an arbitrary number n by:
        - 1st proving it's true when n is 1 and then 
        - assuming it's true for n = k and showing it's true for n = k + 1
    - [For more details](http://comet.lehman.cuny.edu/sormani/teaching/induction.html)
- **Proofs  by contradiction**
    - It allow to prove a proposition is valid (true) by showing that assuming the proposition to be false leads to a contradiction
    - [For more details](https://en.wikipedia.org/wiki/Proof_by_contradiction)
- **T(n)** is the number of lines of code executed by an algorithm

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
    - Make a greedy choice
    - Prove that it is a safe choice
    - Reduce to a subproblem
    - Solve the subproblem (Iterate)
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

</details>

<details>
<summary>Divide and Conquer</summary>

</details>

<details>
<summary>Dynamic Programming</summary>

</details>

<details>
<summary>Use Cases</summary>

- Fibonacci: calculate number of populations
- GCD: Cryptography, The study of prime numbers in factorization

</details>

---

## Data Structures Fundamentals

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
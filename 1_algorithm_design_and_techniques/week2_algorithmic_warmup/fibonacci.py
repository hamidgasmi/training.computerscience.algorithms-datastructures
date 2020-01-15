
#Naive Approach
#Time: 2^n?
#Space:
def fibonacciNaiveApproach(n):

    if n == 0: return 0
    elif n == 1: return 1
    else:
        return fibonacciNaiveApproach(n - 1) + fibonacciNaiveApproach(n - 2)

#Approach 2:
#Time: O(n)
#Space: O(n)
def fibonacci2(n, r):

    if n <= 1: r[n] = n
    else:
        if r[n - 1] == -1: fibonacciNaiveApproach(n - 1, r)
        if r[n - 2] == -1: fibonacciNaiveApproach(n - 2, r)
        r[n] = r[n - 1] + r[n - 2]

#Approach 3:
#Time: O(n)
#Space: O(n) recursion space
def fibonacci3(n, r):

    if n <= 1: return n
    else:
        if r[1] == -1: r[1] = fibonacci3(n - 1, r)
        if r[0] == -1: r[0] = fibonacci3(n - 2, r)
        f = r[1] + r[0]
        r[0] = r[1]
        r[1] = f
        return  f

#Approach 4:
#Time: O(n)
#Space: O(1)
def fibonacci4(n):

    if n <= 1: return n
    else:
        f_n_2 = 0
        f_n_1 = 1
        for i in range(2, n + 1):
            f = f_n_1 + f_n_2
            f_n_2 = f_n_1
            f_n_1 = f
        return  f

n = int(input("Enter a number n: "))


#fib1_Naiveapproach = fibonacciNaiveApproach(n)
#print(fibNaiveapproach)

#Approach 2
#r = [-1] * (n + 1)
#fibonacciNaiveApproach(n, r)
#print(r[n])

#Approach 3
#r = [-1] * 2
#fib3 = fibonacci3(n, r)
#print("Fib 3", fib3)

#Approach 4:
fib4 = fibonacci4(n)
print("Fib 4", fib4)
#assert(fib4 == fib3)
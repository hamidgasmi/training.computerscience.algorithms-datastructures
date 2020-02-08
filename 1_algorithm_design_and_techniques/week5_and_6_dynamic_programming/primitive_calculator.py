import sys

def get_sequence(n, sequenceResult):
    if n >= len(sequenceResult):
        return []

    sequence = []
    while n >= 1:
        sequence.append(n)
        n = sequenceResult[n]

    return reversed(sequence)

def optimal_sequence(n):
    
    operationNbr = [0 for i in range(n + 1)]
    sequenceResult = [0 for i in range(n + 1)]
    for i in range(2, min(4, n + 1)):
        operationNbr[i] = 1
        sequenceResult[i] = 1

    for i in range(4, n + 1):
        oprNbr3 = 1 + operationNbr[i // 3] if i % 3 == 0 else 10 ** 6
        oprNbr2 = 1 + operationNbr[i // 2] if i % 2 == 0 else 10 ** 6
        oprNbr1 = 1 + operationNbr[i - 1]

        if oprNbr3 == min(oprNbr3, oprNbr2, oprNbr1):
            sequenceResult[i] = i // 3
            operationNbr[i] = oprNbr3
        
        elif oprNbr2 == min(oprNbr2, oprNbr1):
            sequenceResult[i] = i // 2
            operationNbr[i] = oprNbr2

        else:
            sequenceResult[i] = i - 1
            operationNbr[i] = oprNbr1

    return get_sequence(n, sequenceResult)

def get_all_optimal_sequences(n, sequenceResult, operationNbr):
    if n <= 3:
        return operationNbr[n]
    elif operationNbr[n] != 0:
        return operationNbr[n]
        
    oprNbr3 = 10 ** 6 + 1
    oprNbr2 = 10 ** 6 + 1
    oprNbr1 = 10 ** 6 + 1
    if n % 3 == 0:
        if operationNbr[n // 3] == 0:
            get_all_optimal_sequences(n // 3, sequenceResult, operationNbr)

        oprNbr3 = operationNbr[n // 3] + 1
    
    if n % 2 == 0:
        if operationNbr[n // 2] == 0:
            get_all_optimal_sequences(n // 2, sequenceResult, operationNbr)

        oprNbr2 = operationNbr[n // 2] + 1
            
    if n - 1 > 0:
        if operationNbr[n - 1] == 0:
            get_all_optimal_sequences(n - 1, sequenceResult, operationNbr)

        oprNbr1 = operationNbr[n - 1] + 1

    if oprNbr3 == min(oprNbr3, oprNbr2, oprNbr1):
        sequenceResult[n] = n // 3
        operationNbr[n] = oprNbr3

    elif oprNbr2 == min(oprNbr2, oprNbr1):
        sequenceResult[n] = n // 2
        operationNbr[n] = oprNbr2

    else:
        sequenceResult[n] = n - 1
        operationNbr[n] = oprNbr1
        
    return operationNbr[n]

def optimal_sequence_recursive(n):

    operationNbr = [0 for i in range(n + 1)]
    sequenceResult = [0 for i in range(n + 1)]
    for i in range(2, min(4, n + 1)):
        operationNbr[i] = 1
        sequenceResult[i] = 1

    get_all_optimal_sequences(n, sequenceResult, operationNbr)

    return get_sequence(n, sequenceResult)

if __name__ == '__main__':

    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
        
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')

#python3 primitive_calculator.py <<< "0"
#python3 primitive_calculator.py <<< "1"
#python3 primitive_calculator.py <<< "2"
#python3 primitive_calculator.py <<< "3"
#python3 primitive_calculator.py <<< "4"
#python3 primitive_calculator.py <<< "5"
#python3 primitive_calculator.py <<< "7"
#python3 primitive_calculator.py <<< "13"
#python3 primitive_calculator.py <<< "17"
#python3 primitive_calculator.py <<< "96234"
#python3 primitive_calculator.py <<< "8192"
#python3 primitive_calculator.py <<< "65536"
#python3 primitive_calculator.py <<< "531441

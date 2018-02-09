computed_values = {
        0: 0,
        1: 1,
        2: 1
    }

def fibonacciDP_not_optimized(n):
    results = {
            0: 0,
            1: 1,
            2: 1
        }
    for i in range(3, n + 1):
        results[i] = results[i-1] + results[i-2]
    return results[n]

def fibonacciDP(n):
    n1 = 0
    n2 = 1
    current = 0
    for i in range(1, n + 1):
        current = n1 + n2
        n2 = n1
        n1 = current
    return current

def fibonacci(n):
    try:
        return computed_values[n]
    except KeyError:
        pass
    new_value = fibonacci(n-1) + fibonacci(n-2)
    computed_values[n] = new_value
    return new_value

def fibonacci_not_optimized(n):
    if(n < 3):
        return 1
    return fibonacci_not_optimized(n-2) + fibonacci_not_optimized(n-1)

def main(i):
    print("fibonacciDP[" + str(i) + "]: " + str(fibonacciDP(i)))
    print("fibonacci[" + str(i) + "]: " + str(fibonacci(i)))
    
    if(i < 101):
        main(i + 1)

main(0)
exit()

# return type function

def fibo():
    fib = [0, 1]
    for i in range(2, 15):
        fib.append(fib[-1] + fib[-2])
    return fib

def sum_fibo():
    fib = fibo()
    return sum(fib)

if __name__ == '__main__':
    print(fibo())
    print(sum_fibo())
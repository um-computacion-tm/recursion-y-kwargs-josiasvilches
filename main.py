def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def factoriales (n):
    if n == 0:
        return 1
    return n * factoriales(n-1)

    
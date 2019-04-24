# 
# even_fibonacci.py
# 

# By considering the terms in the Fibonacci sequence whose values 
# do not exceed four million, find the sum of the even-valued terms.

def main(n: int) -> int: 

    fib_prev = 0
    fib_next = 1
    fib_list = []

    while fib_next <= n:

        fib_prev, fib_next = fib_next,  fib_next + fib_prev
        
        if fib_next <= n: 
            fib_list.append(fib_next)

    even_fib = [k for k in fib_list if k % 2 == 0]
    sum_even_fibs = sum(even_fib, 0) 

    return sum_even_fibs


if __name__ == '__main__':
    k = 4000000
    fibs_sum = main(k)
    print("sum of even Fibonacci numbers with values less then {} is {}".format(k, fibs_sum))
    
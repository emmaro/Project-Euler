# 
# prime_factors.py
# 

# What is the largest prime factor of the number 600851475143 ?


def is_prime(n: int) -> int:
    """
        checks whether a given int is a prime number
    """
    bool = True

    if (n > 2):
        for div in range(2, n):
            if n % div == 0:
                bool = False
                break
    
    return bool


def main(n: int, fac_lst: list) -> int: 
    
    # check if n is prime

    prime = is_prime(n)
    max_prime_fac = None

    if prime:
        max_prime_fac = n 
        fac_lst.append(max_prime_fac)
    else:
        for div in range(2, n):
            if n % div == 0:
                # update n
                k = int(n / div)
                # append factor to list
                fac_lst.append(div)
                main(k, fac_lst)
    

    return max_prime_fac


if __name__ == "__main__":
    facs = []
    k = 6
    max_prime_fac = main(k, facs)
    print(facs)
    
    print(max_prime_fac)
# Find the sum of all the multiples of 3 or 5 below 1000.

def main(n: int) -> int:
    
    range_n = list(range(n))
    
    multiples3 =  [el for el in range_n if el % 3 == 0]
    multiples5 =  [el for el in range_n if el % 5 == 0]

    union = multiples3 + multiples5
    
    unique_list = set(union)

    sum_unique_list = sum(list(unique_list), 0)

    return sum_unique_list


if __name__ == '__main__':
    
    multiples_sum = main(1000)
    print(multiples_sum)
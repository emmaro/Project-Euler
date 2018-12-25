# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

# diff_square,py

 

def square(val):

    return val * val

 

def sum_squares(n):

    ret = 0

    for i in range(n + 1):

        ret += square(i)

       

    return ret

 

def square_sum(n):

   

    vals = list(range(n+1))

    val_sum = sum(vals)

    return val_sum * val_sum

 

if __name__ == '__main__':

    val1 = sum_squares(100)

    print('sum_squares: {}'.format(val1))

    val2 = square_sum(100)

    print('square_sum: {}'.format(val2))

    diff = val2 - val1

    print('square_sum - sum_squares: {}'.format(diff))

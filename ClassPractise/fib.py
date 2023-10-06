def fib(fib_term):

    if (fib_term == 1 or fib_term == 1):
        return 1
    
    count = 0
    prev_num, curr_num = 1, 1
    while (count < fib_term):
        print(curr_num)
        sum = prev_num + curr_num
        prev_num = curr_num
        curr_num = sum
        count += 1

fib(10)

def continue_fibonacci_sequence(sequence, n): 
    for i in range(n): 
        next_element = sequence[-1] + sequence[-2] 
        sequence += [next_element]
# мы должны менять уже имеющуюся переменную, а не создавать новую
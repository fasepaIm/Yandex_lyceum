def rec_linear_sum(some_list):
    if some_list == []:
        return 0
    else:
        return some_list[0] + rec_linear_sum(some_list[1:])
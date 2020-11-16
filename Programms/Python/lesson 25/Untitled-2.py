def recursive_len(some_list):
    if some_list == []:
        return 0
    else:
        return 1 + recursive_len(some_list[:-1])
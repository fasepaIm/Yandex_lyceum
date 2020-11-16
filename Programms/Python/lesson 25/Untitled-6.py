def linear(some_list):
    if not some_list:
        return some_list
    elif isinstance(some_list[0], list):
        return linear(some_list[0][:] + some_list[1:])
    else:
        return [some_list[0]] + linear(some_list[1:])
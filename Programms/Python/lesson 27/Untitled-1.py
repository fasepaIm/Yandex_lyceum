def dec(old_func):
    def new_func(*lol):
        old_func(*[i.upper() for i in lol])    
    return new_func


print = dec(print)
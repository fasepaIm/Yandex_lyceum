def fun(a, b=False, parameter=False):
    if b and not parameter:
        for i in a:
            a[i] += b[i]
    elif b and parameter:
        z = list(a)
        return parameter(z)
    else:
        for i in a:
            a[i] **= 2
    return a


a = {1: 5, 2: 2, 3: 10}
b = {1: 2, 2: 8, 3: 40}
print(fun(a, b, parameter=lambda z: a[z] + b[z]))
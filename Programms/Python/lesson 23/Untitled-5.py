def partial_sums(*el):
    end = [0]
    z = 0
    for i in el:
        z += i
        end.append(z)
    return end
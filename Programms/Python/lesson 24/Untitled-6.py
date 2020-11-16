def find_farthest_orbit(list_of_orbits):
    p = 3.14159265359
    list_of_orbits = list(filter(lambda x: x[0] != x[1], list_of_orbits))
    s = [p * i[0] * i[1] for i in list_of_orbits]
    return list_of_orbits[s.index(max(s))]
import numpy as np
from fractions import Fraction

with open('pipes.txt') as times:
    times = times.readlines()
    pipes = times[-1].split()
    times = [round(float(i.rstrip()) * 60) for i in times[:-2]]
    times = [times[int(i) - 1] for i in pipes]
fractions_list = [Fraction(1, i) for i in times]
lcm = np.lcm.reduce([fr.denominator for fr in fractions_list])
vals = [int(fr.numerator * lcm / fr.denominator) for fr in fractions_list]
vals.append(lcm)
end = open('time.txt', mode='w')
end.write(str(vals[-1] / sum(vals[:-1])))
end.close()

from math import sqrt

file_1, file_2 = input(), input()
usl = open(f'{file_1}', encoding='utf-8', mode='r')
usl_1, usl_2 = [i.rstrip() for i in usl.readlines()]
usl.close()
points_f = open(f'{file_2}', encoding='utf-8', mode='r')
points = [i.rstrip().split() for i in points_f]
points_after_filter = list(filter(lambda n: eval(usl_1.replace('x', str(n[0]))) and eval(usl_2.replace('y', str(n[1]))), points))
len_points = [sqrt(float(i[0]) ** 2 + float(i[-1]) ** 2) for i in points_after_filter]
points = {}
for i in range(len(len_points)):
    points[len_points[i]] = points_after_filter[i]
points_f = sorted(points)
for i in range(len(len_points)):
    points_after_filter[i] = points[points_f[i]] + [points_f[i]]
result = open('answer.txt', encoding='utf-8', mode='w')
for i in points_after_filter:
    result.write(f'({i[0]}, {i[1]}, {i[2]})\n')
result.close()

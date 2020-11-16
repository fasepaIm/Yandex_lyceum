with open('pipes.txt') as times:
    times = times.readlines()
    pipes = times[-1].split()
    times = [[1, round(float(i.rstrip()) * 60)] for i in times[:-2]]
    times = [times[int(i) - 1] for i in pipes]
    one = times[0]
    del times[0]
    while times:
        one = [one[0] * times[0][-1] + times[0][0] * one[-1], one[-1] * times[0][-1]]
        del times[0]
end = open('time.txt', mode='w')
end.write(str(one[-1] / one[0]))
end.close()

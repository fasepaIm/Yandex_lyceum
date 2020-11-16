from hurry.filesize import size, si

extensions = {}
files_size = {}
extension = []
size_f = {
    "B": 1, "KB": 1024, "MB": 1048576, "GB": 1073741824, "TB": 1099511627776, "PB": 1125899906842624
}
file = open('input.txt')
files = file.readlines()
for i in files:
    if i.split()[0].split('.')[-1] not in extensions:
        extensions[i.split()[0].split('.')[-1]] = [i.split()[0]]
        extension.append(i.split()[0].split('.')[-1])
    else:
        extensions[i.split()[0].split('.')[-1]] += [i.split()[0]]
    files_size[i.split()[0]] = float(i.split()[1]) * size_f[i.split()[-1]]
extension.sort()
for i in extension:
    extensions[i].sort()
out = open('output.txt', mode='w')
for i in extension:
    sizes = 0
    for j in extensions[i]:
        out.write(f'{j}\n')
    out.write('----------\n')
    for j in extensions[i]:
        sizes += int(files_size[j])
    out.write(f'Summary: {size(sizes, system=si)}\n')
    out.write('\n')
out.close()

extensions = {}
files_size = {}
extension = []
size_f = {
    "B": 1, "KB": 1024, "MB": 1048576, "GB": 1073741824
}
size_name = ['GB', 'MB', 'KB', 'B']
file = open('input.txt')
files = file.readlines()
for i in files:
    if i.split()[0].split('.')[-1] not in extensions:
        extensions[i.split()[0].split('.')[-1]] = [i.split()[0]]
        extension.append(i.split()[0].split('.')[-1])
    else:
        extensions[i.split()[0].split('.')[-1]] += [i.split()[0]]
    if i.split()[0] not in files_size:
        files_size[i.split()[0]] = int(float(i.split()[1]) * size_f[i.split()[-1]])
    else:
        files_size[i.split()[0]] += int(float(i.split()[1]) * size_f[i.split()[-1]])
extension.sort()
for i in extension:
    extensions[i].sort()
out = open('output.txt', mode='w')
for i in extension:
    write = []
    sizes = 0
    for j in extensions[i]:
        out.write(f'{j}\n')
    out.write('----------\n')
    for j in extensions[i]:
        if j not in write:
            sizes += int(files_size[j])
            write.append(j)
    for m in size_name:
        if sizes / size_f[m] >= 1:
            sizes = round(sizes / size_f[m])
            break
    out.write(f'Summary: {sizes} {m}\n')
    out.write('\n')
out.close()

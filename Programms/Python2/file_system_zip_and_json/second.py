import os


def get_files_sizes():
    names = os.listdir()
    info = []
    for name in names:
        if os.path.isfile(name):
            it = 0
            sizes = {
                0: 'Б',
                1: 'КБ',
                2: 'МБ',
                3: 'ГБ',
            }
            size = os.path.getsize(name)
            while size // 1024 > 0:
                size /= 1024
                it += 1
            info.append(f'{name} {round(size)}{sizes[it]}\n')
    return ''.join(info)


print(get_files_sizes())

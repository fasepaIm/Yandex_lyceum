def human_read_format(size):
    it = 0
    sizes = {
        0: 'Б',
        1: 'КБ',
        2: 'МБ',
        3: 'ГБ',
    }
    while size // 1024 > 0:
        size /= 1024
        it += 1
    return f'{round(size)}{sizes[it]}'

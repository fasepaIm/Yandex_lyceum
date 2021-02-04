import sys


voc = {}
data = sys.argv[1:]
if data.count('--sort'):
    data.remove('--sort')
    for i in data[:]:
        string = i.split('=')
        voc[string[0]] = string[1]
    for key in sorted(list(voc.keys())):
        print(f'Key: {key} Value: {voc[key]}')
else:
    for i in data:
        string = i.split('=')
        voc[string[0]] = string[1]
    for key in voc:
        print(f'Key: {key} Value: {voc[key]}')

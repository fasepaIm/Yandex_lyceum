import json
import csv
from operator import itemgetter


with open('mask.json') as cat_file:
    f = cat_file.read()
    data = json.loads(f)
    new_data = []
    for item in data:
        if item["disguise"] < 10:
            new_data.append(item)
    print(new_data)
    print()
    #new_data = sorted(new_data, key=lambda dictionary: (dictionary['disguise'], dictionary['name']), reverse=True)
    new_data = sorted(new_data, key=itemgetter('name'))
    new_data = sorted(new_data, key=itemgetter('disguise'), reverse = True)
    #new_data = sorted(new_data, key=lambda dictionary: dictionary['disguise'], reverse=True)
    #new_data = sorted(new_data, key=lambda dictionary: dictionary['name'])
    #new_data = sorted(new_data, key=lambda elem: "%02d %s" % (elem['disguise'], elem['name']), reverse=True)
    print(new_data)
    with open('invisible.csv', 'w', newline='') as csvfile:
        writer = csv.writer(
            csvfile, delimiter=';', quotechar='"',
            quoting=csv.QUOTE_MINIMAL)
        writer.writerow([i for i in new_data[0]])
        for i in range(len(new_data)):
            writer.writerow([new_data[i][name] for name in new_data[i]])

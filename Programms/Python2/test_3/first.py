import sys
import json


vocabluary = {}
constant = {}
varying = {}

data = list(map(str.strip, sys.stdin))
for i in data:
    string_list = i.split("#")
    if 15 < int(string_list[-1]) < 100:
        constant[string_list[0][:-1]] = string_list[-1][1:]
    else:
        varying[string_list[0][:-1]] = string_list[-1][1:]

vocabluary["constant"] = constant
vocabluary["varying"] = varying

with open('orbit.json', 'w') as json_file:
    json.dump(vocabluary, json_file)

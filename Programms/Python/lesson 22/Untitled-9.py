def from_string_to_list(string, container):
    string = string.split()
    for i in string:
        if i.isdigit():
            container += [i]
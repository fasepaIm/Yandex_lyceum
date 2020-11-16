friends = {}


def add_friends(name_of_person, list_of_friends):
    global friends
    if name_of_person in friends:
        a = friends[name_of_person]
        for i in list_of_friends:
            a.append(i)
        friends[name_of_person] = a
    else:
        friends[name_of_person] = list_of_friends


def are_friends(name_of_person1, name_of_person2):
    global friends
    if name_of_person2 in friends[name_of_person1]:
        return True
    else:
        return False
    

def print_friends(name_of_person):
    global friends
    names = friends[name_of_person]
    names.sort()
    print(*names)
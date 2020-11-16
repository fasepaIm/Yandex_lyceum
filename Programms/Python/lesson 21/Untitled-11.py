def lucky(ticket):
    global lastTicket
    a = []
    b = []
    z = 0
    x = 0
    lastTicket = str(lastTicket)
    if len(lastTicket) < 6:
        lol = 6 - len(lastTicket)
    for i in lastTicket:
        if len(lastTicket) < 6 and z == 0:
            for j in range(lol):
                a.append('0')
                z = 1
        a.append(i)
    ticket = str(ticket)
    if len(ticket) < 6:
        lolol = 6 - len(ticket)
    for i in ticket:
        if len(ticket) < 6 and x == 0:
            for j in range(lolol):
                b.append('0')
                x = 1
        b.append(i)
    first_ticket, second_ticket, first_ticket2, second_ticket2 = 0, 0, 0, 0
    for j in range(3):
        first_ticket += int(a[j])
        first_ticket2 += int(b[j])
    for i in range(-1, -4, -1):
        second_ticket += int(a[i])
        second_ticket2 += int(b[i])
    if first_ticket == second_ticket and first_ticket2 == second_ticket2:
        return 'Счастливый'
    else:
        return 'Несчастливый'
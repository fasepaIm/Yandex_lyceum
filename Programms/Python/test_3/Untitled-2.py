def collecting_lilies(full_moon, n):
    date_day = dt.date(2020, 1, 1) #dt.datetime.now().date()
    full_moon = [int(i) for i in full_moon.split('.')]
    full_moon = [full_moon[-1], full_moon[1], full_moon[0]]
    full_moon = dt.date(*full_moon)
    date_day = date_day + dt.timedelta(days=int(n))   
    if full_moon == date_day:
        date_day = date_day + dt.timedelta(days=2)
    return ' '.join([str(date_day), date_day.strftime("%w")])
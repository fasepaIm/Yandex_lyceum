def date_analysis(dates):
    years = []
    autumn = ['09', '10', '11']
    dates = list(filter(lambda x: x.split('-')[1] not in autumn, dates))
    for i in dates:
        years.append(i.split('-')[-3])
    years = max(years)
    dates = list(filter(lambda x: x.split('-')[-3] == years, dates))
    month = []
    for i in dates:
        month.append(i.split('-')[-2])
    month = max(month)
    dates = list(filter(lambda x: x.split('-')[-2] == month, dates))
    days = []
    for i in dates:
        days.append(i.split('-')[-1])
    days = max(days)
    dates = list(filter(lambda x: x.split('-')[-1] == days, dates))
    return dates[-1]
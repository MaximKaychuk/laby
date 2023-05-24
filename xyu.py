name_dict = {
    'ПОНЕДЕЛЬНИК': 'Monday',
    'ВТОРНИК': 'Tuesday',
    'СРЕДА': 'Wednesday',
    'ЧЕТВЕРГ': 'Thursday',
    'ПЯТНИЦА': 'Friday',
    'СУББОТА': 'Saturday',
}

file = list(open('text.txt', encoding='utf8'))

name = name_dict[file[0].split()[0]]

days = [[]]
for row in file[1::]:
    if len(row.split()) == 0:
        days.append([])
    else:
        days[-1].append(' '.join(row.split()))

pars = [day[1::] for day in days]

for par in pars:
    res = par.copy()
    if len(res) == 1:
        res = res * 3
    res = ', '.join(res)
    print(f"INSERT INTO timetable_even ({name}) VALUES ('{res}');")
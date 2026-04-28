import numpy as np
from scipy.optimize import linear_sum_assignment

with open('dates.csv') as f:
    a = f.read().strip().split('\n')
a = [i.split(',') for i in a]
def parse_interview(row):
    name = row[0]
    maybe_priority = row[-1].strip()
    if len(row) >= 3:
        try:
            return name, set(row[1:-1]), float(maybe_priority)
        except ValueError:
            pass
    return name, set(row[1:]), 1

interviews = [parse_interview(row) for row in a if row and row[0].strip()]
dates = sorted(set().union(*(i[1] for i in interviews)))
keys = [i[0] for i in interviews]
values = [i[1] for i in interviews]
priorities = [i[2] for i in interviews]

n = len(dates)
encode = lambda x, p: [p if dates[i] in x else 0 for i in range(n)]
matrix = np.array([encode(v, p) for v, p in zip(values, priorities)]).astype(np.float64)

row_ind, col_ind = linear_sum_assignment(-matrix)
print(len(row_ind))
assigned_dates = {}
for (i, j) in zip(row_ind, col_ind):
    print(keys[i],':', dates[j])
    assigned_dates[dates[j]] = assigned_dates.get(dates[j], 0) + 1

duplicate_dates = [f"{date} ({count})" for date, count in assigned_dates.items() if count > 1]
if duplicate_dates:
    print('Note: multiple interviews were assigned the same date:', ', '.join(duplicate_dates))

row_ind_set = set(row_ind)
for (i, j) in enumerate(keys):
    if i not in row_ind_set:
        print(j, end=', ')

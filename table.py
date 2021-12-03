from prettytable import PrettyTable

from data import dt,th
columns=len(th)
table=PrettyTable(th)

dt_data=dt[:]
while dt_data:
    columns=5
    table.add_rows(dt_data[:columns])
    dt_data=dt_data[columns:]


def opentabble():
    print('Аналіз основних показників діяльності підприємств')
    print(table)
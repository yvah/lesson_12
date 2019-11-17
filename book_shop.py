from random import randint

lst = [
    [randint(1, 99999), 'Learning Python, Mark Lutz', randint(1, 10), 40.95],
    [randint(1, 99999), 'Programming Python, Mark Lutz', randint(1, 10), 56.80],
    [randint(1, 99999), 'Head First Python, Paul Barry', randint(1, 10), 32.95],
    [randint(1, 99999), 'Einführung in Python3, Bernd Klein', randint(1, 10), 24.99]
]

table = '+--------------+------------------------------------+----------+-------------+\n'
print(table, '| Order Number |       Book Title and Author        | Quantity | Order Price |\n', table, sep='')

result = list(map(lambda x: (x[0], round(x[2]*x[3], 2) if x[2]*x[3] >= 100 else round(x[2]*x[3] + 10, 2)), lst))
print(result)

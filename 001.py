""" 1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
наименования предприятий, чья прибыль ниже среднего.
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из
модуля collections
"""

from collections import namedtuple


Enterprise = namedtuple('Enterprise', 'name quarter_1 quarter_2 quarter_3 quarter_4 year')

enterprise_count = int(input('Введите количество предприятий: '))
enterprises = [0 for _ in range(enterprise_count)]
profit_sum = 0

for i in range(enterprise_count):
    name = input(f'Введите название {i+1}-го предприятия: ')
    quarters = [float(j) for j in input('Введите прибыль в каждом квартале через пробел: ').split()]

    year = 0
    for quarter in quarters:
        year += quarter

    profit_sum += year
    enterprises[i] = Enterprise(name, *quarters, year)
    # print(enterprises[i])

if enterprise_count == 1:
    print(f'Предприятие: {enterprises[0].name}. Годовая прибыль: {enterprises[0].year}')

else:
    profit_average = profit_sum / enterprise_count

    less = []
    more = []

    for i in range(enterprise_count):

        if enterprises[i].year < profit_average:
            less.append(enterprises[i])

        elif enterprises[i].year > profit_average:
            more.append(enterprises[i])

    print(f'\nСредняя годовая прибыль предприятий: {profit_average: .2f}')

    print(f'Предприятия, чья прибыль меньше среднего:')
    for ent in less:
        print(f'Предприятие "{ent.name}" с прибылью {ent.year: .2f}')

    print(f'\nПредприятия, чья прибыль больше среднего:')
    for ent in more:
        print(f'Предприятие "{ent.name}" с прибылью {ent.year: .2f}')

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
per_cent_values = list(per_cent.values())
deposit = [value * money for value in per_cent_values]
print(f'deposit = {deposit}')
print(f'Максимальная сумма, которую вы можете заработать - {max(deposit)}')
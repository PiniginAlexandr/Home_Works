my_dict = {
    'Alexandr': 2001,
    'Mark': 1978,
    'Egor': 1939
}
print('Словарь:', my_dict)
print(f'Существующий ключ словаря:'
      f' {my_dict['Alexandr']}'
      f'\nОтсутствующий ключ:'
      f' {my_dict.get('Nail')}')
my_dict.update({'Vladislava': 2004, 'Yulia': 1939})
print(f'Добавлено два элемента: {my_dict}')
dict_remove = my_dict.pop('Alexandr')
print(f'Значение удаленного ключа: {dict_remove}\n')

my_set = {1, 2, 1, 2, 3, 3, 4, 'str', 'int', 'str', True}
print(f'Уникальные множества: {my_set}')
new_add = {5, 'Milk'}
my_set.update(new_add)
print(f'Добавлено два элемента: {my_set}')
my_set.discard('str')
print(f'Итоговый множества после удаления: {my_set}')
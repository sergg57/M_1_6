# работа со словарями
my_dict = {'Mike': 1935, 'Pit': 2004, 'Nina': 1978, 'Fred': 2020}
print(type(my_dict),'\n',  'Dict: ', my_dict)
print('Existing vale: ', my_dict['Nina'])
print('No existing vale: ', my_dict.get('Vasya'))
my_dict.update({'Vasya':2011,
                    'Anna': 1992})
print('Modified dictionary: ', my_dict)
print('Deleted value:', my_dict.pop('Fred'))
print('Dictionary after deleted value:',  my_dict)

# работа с множествами
print('\n')
my_set = {5, 4, 5, 4, 'Alex', 'Apple', 'Apple', 'Alex', True, False, False }
print(type(my_set), '\n', 'Set: ', my_set)
#my_set.add(6)
#my_set.add('Anton')
my_set.update([6, 'Anton'])
print('Modified set: ',my_set)
my_set.discard(False)
print('Set after deleted value - "False":', my_set)
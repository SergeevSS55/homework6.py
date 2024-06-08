my_dict = {'Sergei' : 1998,
           'Anna' : 1997,
           'Mikhail' : 2024}
print(my_dict['Sergei'])
my_dict['Dmitry'] = 1990
print(my_dict['Dmitry'])
my_dict.update({'Egor' : 2010,
                'Larisa' : 1975})
comeback = my_dict.pop('Anna')
print(comeback)
print(my_dict)
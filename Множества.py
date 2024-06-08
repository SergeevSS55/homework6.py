list_ = [1, 2, 3, 55, True, 'apple', 'apple', 3, 55, 'banana']
my_set = set(list_)
print(my_set)
my_set.add(144)
my_set.add('melon')
print(my_set.discard(3), print(my_set.remove('apple')))
print(my_set)
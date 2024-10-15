immutable_var = 1, 'str', True, 1.5, [1,5,7]
immutable_var [4][0] = ('list')
#В кортеже допускается изменение только изменяемыж объектов.
#int, str, bool, float относятся к неизменяемым объектам.
print(immutable_var)

mutable_list = [1,'str', True, 1.5, [1,5,7]]
mutable_list [0] = 'str'
mutable_list [1] = True
mutable_list [2] = 1
mutable_list [3] = [1,5,7]
mutable_list [4] = 1.5
mutable_list.append('Mudified')
print(mutable_list)
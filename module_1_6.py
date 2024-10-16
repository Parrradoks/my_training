my_dict = {'Nikita':1999, 'Anastasia':2000, 'Max':2026,'Robert':2026}
print(my_dict)
print(my_dict.get('Max'),my_dict.get('Anna','Такого человека не числится'))
my_dict.update({'Anna':2002,'Bob':1956})
print(my_dict)
my_dict.pop('Anna')
print(my_dict)
#my_dict.pop('Bob') #По отдельности команды выполняются, а вместе нет. Пожалуйста, объясните как можно
#print(my_dict)     #сделать так, чтобы одновременно можно было удалить и вывести удленное значение.
a = my_dict.pop('Bob') #Нужных методов не нашел, перепробовал разные варианты и компановки
print(a)               #в лекции данный вопрос не разбирался.


my_set = {1,1,1,'str','str',1.5}
print(my_set)
my_set.update({(1,2,3),'Nik'})
#my_set.add((1,2,3))  Если использовать метод ".add()", то добавляется один элемент, поэтому использую ".update()"
#my_set.add('Nik')
print(my_set)
my_set.remove('Nik')
print(my_set)
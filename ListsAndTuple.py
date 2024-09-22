immutable_var = 'Roman', 2, 'суп', 4, 10
#immutable_var[2] = 7 Ошибка сообщает нам, что кортеж не поддерживает обращение по элементам
print(immutable_var)
mutable_list = ['Roman', 2, 'суп', 4, 10]
mutable_list[0] = 100
print(mutable_list)
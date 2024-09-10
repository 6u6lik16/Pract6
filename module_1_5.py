immutable_var = 24, "Сергей", True, 102.2
print(immutable_var)
#immutable_var[1] = "Антон" - изменить элементы кортежа мы не можем, т к кортеж относиться к неизменяемым типам данных,
# но если в нём находяться изменяемые типы данных как например list(список),
# то его мы уже можем изменять внутри кортежа
mutable_list = ["Алина", 124, False]
print(mutable_list)
mutable_list[2] = True
mutable_list[1] = 0
mutable_list[0] = "Serg"
print(mutable_list)
from functional import create
from interface import interface
path = "phone_book.txt"
create(path)
enter = 0
while enter != 6:
    enter = interface()
    if enter == 1:
        from functional import add_cont
        stroka = str(input("Введите ФИО и номер телефона через пробел: "))
        add_cont(path, stroka)
    elif enter == 2:
        from functional import show_all
        print(show_all(path))
    elif enter == 3:
        from functional import search
        stroka = str(input("Введите фамилию: "))
        search(path, stroka)
    elif enter == 4:
        from functional import delete
        stroka = str(input("Введите значение для удаления: "))
        delete(path, stroka)
    elif enter == 5:
        from functional import change
        stroka = str(input("Введите значение для изменения: "))
        change(path, stroka)
print("Cпасибо за работу! ")
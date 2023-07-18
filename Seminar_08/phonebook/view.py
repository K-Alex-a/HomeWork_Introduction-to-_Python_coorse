def menu() -> int:
    while True:
        print('Возможные действия:\n'
              '1 - Создать запись\n'
              '2 - Вывести имеющиеся данный в консоль\n'
              '3 - Экспортировать данные\n'
              '4 - Импортировать данные\n'
              '5 - Найти контакты\n'
              '6 - Изменить данные\n'
              '7 - Удалить данные\n'
              '8 - Выход\n')
        user_input = int(input('Введите цифру действия => '))
        print()
        return user_input


def get_user_data() -> tuple:
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    discrip = input('Введите описание: ')
    print()
    return surname, name, phone, discrip


def list_values() -> None:
    print('\nПараметры для изменения:\n'
          '1 - Фамилия\n'
          '2 - Имя\n'
          '3 - Номер телефона\n'
          '4 - Описание\n')


def get_value():
    value = input('Введите искомое значение: ')
    print()
    return value


def get_operation_id() -> int:
    delete_item = int(input('Введите id (номер) строки с которой будут проводится операции: '))
    print()
    return delete_item


def get_change_item() -> int:
    list_values()
    change_item = int(input('Введите номер параметра, которое будем менять => '))
    print()
    return change_item


def get_new_value() -> str:
    new_value = input('Введите новое значение: ')
    return new_value


def not_found_value() -> None:
    print(f'{"=" * 40}\nЗапись не найдена!\n{"=" * 40}\n')







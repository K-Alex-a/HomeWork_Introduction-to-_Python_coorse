def create(db: dict, _id: int, surname: str, name: str, phone: str, discrip: str) -> tuple:
    db[_id] = {'surname': surname, 'name': name, 'phone': phone, 'discrip': discrip}
    _id += 1
    return db, _id


def print_data(db: dict) -> None:
    print('{:<3} {:<15} {:<15} {:<15} {:<15}'.format('ID', 'Surname', 'Name', 'Phone', 'Discrip'))
    for _id in db:
        print(
            f'{_id:<3} {db[_id]["surname"]:<15} {db[_id]["name"]:<15} {db[_id]["phone"]:<15} {db[_id]["discrip"]:<15}')
    print()


def export_db(db: dict, filepath: str, delimiter: str = ',') -> None:
    with open(filepath, 'w', encoding='UTF-8') as file:
        for _id, data in db.items():
            file.write(
                f"{data['surname']}{delimiter}{data['name']}{delimiter}{data['phone']}{delimiter}{data['discrip']}\n")


def import_db(db: dict, _id: int, filepath: str, delimiter: str = ',') -> tuple:
    with open(filepath, 'r', encoding='UTF-8') as file:
        for line in file:
            data = line.strip().split(delimiter)
            db[_id] = {'surname': data[0], 'name': data[1], 'phone': data[2], 'discrip': data[3]}
            _id += 1
    return db, _id


def selection_values(item: int) -> str:
    if item == 1:
        item = 'surname'
    elif item == 2:
        item = 'name'
    elif item == 3:
        item = 'phone'
    elif item == 4:
        item = 'discrip'
    else:
        print('Not found')
    return item


def found_surname(db: dict, _id: int, search_item: str) -> int:
    search_item = search_item.lower()
    for _id in db:
        if search_item in db[_id]['surname'].lower() \
                or search_item in db[_id]['name'].lower() \
                or search_item in db[_id]['phone'].lower() \
                or search_item in db[_id]['discrip'].lower():
            print(f'{db[_id]}')
    print()


def delete_line(db: dict, _id: int) -> dict:
    return db.pop(_id)


def change_line(db: dict, _id: int, item: int, get_item: str) -> dict:
    item = selection_values(item)
    db[_id][item] = get_item
    return db





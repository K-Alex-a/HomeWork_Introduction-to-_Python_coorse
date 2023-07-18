from functions_base import *
from view import *

phonebook = {}
phonebook_last_id = 0


def main(db: dict, last_id: int) -> None:
    while True:
        menu_item = menu()
        match menu_item:
            case 1:
                record_contact = get_user_data()
                db, last_id = create(db, last_id, *record_contact)
            case 2:
                print_data(db)
            case 3:
                export_db(db, 'data_base.txt')
            case 4:
                db, last_id = import_db(db, last_id, 'data_base.txt')
            case 5:
                found_surname(db, last_id, get_value())
            case 6:
                change_id = get_operation_id()
                change_item = get_change_item()
                change_line(db, change_id, change_item, get_new_value())

            case 7:
                delete_item = get_operation_id()
                delete_line(db, delete_item)
            case 8:
                break


main(phonebook, phonebook_last_id)

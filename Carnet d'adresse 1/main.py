from contact_class import *
from interface_class import *
from utils import clear_console

contact_file = 'fiches.json'

manager = Contact(contact_file)
interface = Interface(manager)

while True:
    clear_console()
    choice = interface.show_menu()

    match choice:
        case '1':
            interface.create()
        case '2':
            while True:
                clear_console()
                choice_contact = interface.show_contacts_list()
                if choice_contact == 'Q' or choice_contact == 'q':
                    break
                
                while True:
                    choice_management = interface.show_contact(choice_contact)

                    match choice_management:
                        case '1':
                            interface.update(choice_management)
                        case '2':
                            interface.delete(choice_contact)
                            break
                        case 'Q':
                            clear_console()
                            break
                        case 'q':
                            clear_console()
                            break
                        case _:
                            pass
        case 'q':
            break
        case 'Q':
            break
        case _:
            pass
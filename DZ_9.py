import codecs

def work_with_book():
    print("Какое действие выаолнить? ")
    user_choice = input("1 - найти  контакт \n 2 - добавить контакт \n 3 - удалить контакт \n 4 - изменить контакт \n 5 - показать контакты \n 6 - выход \n ")
    print("\n")
    if user_choice == '1':
        find_contact()
    elif user_choice == '2':
        add_contact_phone()
    elif user_choice == '3':
        delete_contact()
    elif user_choice == '4':
        change_contact()
    elif user_choice == '5':
        show_contact()
    elif user_choice == '6':
        exit_program()

def find_contact():
    print('Вы выбрали найти контакт')
    search_contact = str (input("Введите имя или телефон: "))
    search = search_contact
    contacts = get_all_contacts()
    isFound = False
    for contact in contacts:
        if search in contact:
            print(contact, end="")
            isFound = True

    if (isFound == False):
        print("Ничего не найдено")

def add_contact_phone():
    print('Вы выбрали добавить контакт')
    with codecs.open("data.txt", 'a', 'utf-8') as data:
        last_name = input('Введите фамилию: ')
        first_name = input('Введите имя: ')
        phone_number = input('Введите номер телефона: ')
        data.write(last_name + ';' + first_name + ';' + phone_number + "\n")

def delete_contact():
    print('Вы выбрали удалить контакт')
    del_line = int(input("Введите номер строки удаления "))
    contacts = get_all_contacts()

    i = 0
    for contact in contacts:
        if (i + 1) == del_line:
            contacts.pop(i)
            break
        i += 1
    
    save_array_to_file(contacts)


def change_contact():
    print('Вы выбрали изменить контакт')
    in_line = int(input("Введите номер строки редактирования "))
    contacts = get_all_contacts()

    with codecs.open("data.txt", 'a', 'utf-8') as data:
        for line in data:
            if line == in_line:
                last_name = input('Введите фамилию: ')
                first_name = input('Введите имя: ')
                phone_number = input('Введите номер телефона: ')
                data.write(last_name + ';' + first_name + ';' + phone_number + "\n")


def show_contact():
    print('Вы выбрали показать все контакты')

    for line in get_all_contacts():
        print(line, end='')


def get_all_contacts():
    file = codecs.open('data.txt', 'r', 'utf-8')
    data = file.readlines()
    return data

def save_array_to_file(data):
    file = codecs.open('data.txt', 'w', 'utf-8')

    for item in data:
        file.write(item)

    file.close()

def exit_program():
     print('Вы выбрали выйти из приложения')
     exit(1)


work_with_book()
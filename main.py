
def display_records(page_number: int, records_per_page: int = 5) -> None:
    """
        Отображение записей из файла
        По умолчанию считается, что пять записей в файле - это одна страница справочника
    """
    with open("phonebook.txt", "r", encoding='utf-8') as file:
        lines = file.readlines()
        start_index = (page_number - 1) * records_per_page
        end_index = page_number * records_per_page
        for line in lines[start_index:end_index]:
            print(line.strip())

def add_record(last_name: str, first_name: str, middle_name: str, organization: str, work_phone: str, personal_phone: str) -> None:
    """
        Добавление записи в файл
    """
    with open("phonebook.txt", "a", encoding='utf-8') as file:
        file.write(f"{last_name}, {first_name}, {middle_name}, {organization}, {work_phone}, {personal_phone}\n")

def edit_record(last_name: str, new_data: str) -> None:
    """
        Редактирование записи
    """
    with open("phonebook.txt", "r", encoding='utf-8') as file:
        lines = file.readlines()
    with open("phonebook.txt", "w", encoding='utf-8') as file:
        for line in lines:
            if last_name in line:
                file.write(new_data + "\n")
            else:
                file.write(line)

def search_records(query: str) -> None:
    """
        Поиск записи в файле
    """
    with open("phonebook.txt", "r", encoding='utf-8') as file:
        for line in file:
            if query.lower() in line.lower():
                print(line.strip())

def main():
    while True:
        print("1. Вывести записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            page_number = int(input("Введите номер страницы: "))
            display_records(page_number, records_per_page=5)
        elif choice == "2":
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            organization = input("Введите название организации: ")
            work_phone = input("Введите рабочий телефон: ")
            personal_phone = input("Введите личный телефон: ")
            add_record(last_name, first_name, middle_name, organization, work_phone, personal_phone)
        elif choice == "3":
            last_name = input("Введите фамилию для редактирования: ")
            new_data = input("Введите новые данные: ")
            edit_record(last_name, new_data)
        elif choice == "4":
            query = input("Введите запрос для поиска: ")
            search_records(query)
        elif choice == "5":
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")


if __name__ == '__main__':
    main()
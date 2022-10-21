import openpyxl
from openpyxl import load_workbook


# +добавить клиента
def add_client(name: str, sec_name: str, phone: str, spec: str):
    sheet = openpyxl.open("base.xlsx")
    sheet.active = 3
    i = 2
    while sheet.active[f"A{i}"].value:
        i += 1
    sheet.active[f"A{i}"].value = i - 1
    sheet.active[f"B{i}"].value = name
    sheet.active[f"C{i}"].value = sec_name
    sheet.active[f"D{i}"].value = phone
    sheet.active[f"E{i}"].value = spec
    sheet.save('base.xlsx')


# +список всех клиентов
def client_list():
    sheet = openpyxl.open("base.xlsx")
    sheet.active = 3
    i = 2
    while sheet.active[f"A{i}"].value:
        print(
            f'  {sheet.active[f"A{i}"].value}.{sheet.active[f"B{i}"].value} {sheet.active[f"C{i}"].value} {sheet.active[f"D{i}"].value} {sheet.active[f"E{i}"].value}')
        i += 1


def client_selection_id():
    sheet = openpyxl.open("base.xlsx")
    sheet.active = 3
    i = 2
    print("Выберите клиента: ")
    while sheet.active[f"A{i}"].value:
        print(f'  {sheet.active[f"A{i}"].value}.{sheet.active[f"B{i}"].value} {sheet.active[f"C{i}"].value} ')
        i += 1
    print("Введите 0 для добавления клиента!")
    id = int(input(f'Введите цифру клиента: '))
    if id == 0:
        add_client(input("Введите имя клиента: "), input("Введите фамилию клиента: "),
                   input("Введите номер телефона клиента: "), input("Введите описание: "))
        client_selection_id()
    while id > i - 2 or id < 0:
        print("Ошибка!")
        id = int(input(f'Введите цифру клиента: '))

    return id

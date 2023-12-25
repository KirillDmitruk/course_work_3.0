import json
from config import OPERATION_FILE_DIR
from operator import itemgetter

def get_all_operations():
    """
    Получает содержимое из json и возвращает список словарей
    """
    with open(OPERATION_FILE_DIR, 'r', encoding="utf8") as file:
        data = file.read()
        content = json.loads(data)
    return content


def sort_operations(unsorted_list):
    """
    Возвращает отсортированный список с выполненными операциями
    """
    sorted_list = []
    for operation in unsorted_list:
        for key, value in operation.items():
            if value == "EXECUTED":
                sorted_list.append(operation)
    return sorted_list


def sort_descending_order(unsorted_list):
    """
    Возвращает отсортированный по убыванию даты
    """
    sorted_data_list = sorted(unsorted_list, key=itemgetter("date"), reverse=True)
    return sorted_data_list


def correct_format_data(date):
    """
    Возвращает формат ДД.ММ.ГГГГ
     """
    original_data = date[:10]
    data_list = original_data.split("-")
    return '.'.join(data_list[::-1])


def split_text_numbers(bill):
    """
    Функция превращает строку счета в список из названия счета и его номера
    """
    text = ""
    numbers = ""
    res = []
    for i in bill:
        if i.isdigit():
            numbers += i
        else:
            text += i
    res.append(text.strip())
    res.append(numbers)
    return res


def encrypt_bill_num(bill_num):
    """
    Функция, определяющая счет это или карта
    """
    if len(bill_num) == 20:
        return f'**{bill_num[-4:]}'
    elif len(bill_num) == 16:
        return f'{bill_num[:4]} {bill_num[4:6]}** **** {bill_num[-4:]}'


def get_formated_operation(operation):
    """
    Выводит форматированную операцию
    14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
    """
    new_date = correct_format_data(operation['date'])
    description = operation['description']
    amount = operation["operationAmount"]['amount']
    currency = operation["operationAmount"]['currency']['name']

    if not operation['description'] == "Открытие вклада":
        sender = split_text_numbers(operation["from"])
        receiver = split_text_numbers(operation["to"])
        sender[1] = encrypt_bill_num(sender[1])
        receiver[1] = encrypt_bill_num(receiver[1])
        sender_new = " ".join(sender)
        receiver_new = " ".join(receiver)
        return (f'{new_date} {description}\n'
                f'{sender_new} -> {receiver_new}\n'
                f'{amount} {currency}')
    else:
        receiver = split_text_numbers(operation["to"])
        receiver[1] = encrypt_bill_num(receiver[1])
        receiver_new = " ".join(receiver)
        return (f'{new_date} {description}\n'
                f'{receiver_new}\n'
                f'{amount} {currency}')
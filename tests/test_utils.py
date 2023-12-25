from src.utils import get_formated_operation, \
    encrypt_bill_num, split_text_numbers, correct_format_data

operation = {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
        "amount": "41096.24",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
}
operation2 = {
    "id": 114832369,
    "state": "EXECUTED",
    "date": "2019-12-07T06:17:14.634890",
    "operationAmount": {
        "amount": "48150.39",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "Visa Classic 2842878893689012",
    "to": "Счет 35158586384610753655"
}


def test_get_formated_operation():
    assert get_formated_operation(operation) == f"08.12.2019 Открытие вклада\nСчет **5907\n41096.24 USD"
    assert get_formated_operation(
        operation2) == f"07.12.2019 Перевод организации\nVisa Classic 2842 87* *** 9012 -> Счет **3655\n48150.39 USD"


def test_encrypt_bill_num():
    assert encrypt_bill_num('2842878893689012') == "2842 87** **** 9012"
    assert encrypt_bill_num('35158586384610753655') == "**3655"


def test_split_text_numbers():
    assert split_text_numbers("Счет 24763316288121894080") == ['Счет', '24763316288121894080']
    assert split_text_numbers('Visa Platinum 2256483756542539') == ['Visa Platinum', '2256483756542539']


def test_correct_format_data():
    assert correct_format_data("2019-04-18T11:22:18.800453") == "18.04.2019"

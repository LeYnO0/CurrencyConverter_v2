import requests
import json

# Обращаемся по API, превращаем исходную большую строку в один список, внутри которого обращаемся к списку с валютами.
URL = 'https://www.cbr-xml-daily.ru/latest.js'
request = requests.get(URL)
request = request.text
data_dict = json.loads(request)
# Приравниваем новый список к уже существующему, чтобы не исправлять это во всем коде.
EXCHANGE_RATES = data_dict['rates']


def get_exchange_rates():
    return EXCHANGE_RATES


def main():
    exchange_rates = get_exchange_rates()
    keys_list = list(exchange_rates.keys())
    # Убираем кавычки и ставим запятую между аббревиатурой валют.
    keys_string = (", ".join(keys_list))
    base_currency = input(f'Введите валюту, которую хотите обменять: {keys_string}.\n')
    # Приводим вводимое значение к верхнему регистру.
    base_currency_up = base_currency.upper()
    # Проверяем, имеется ли вводимое значение среду ключей словаря валют.
    if base_currency_up not in exchange_rates:
        return print('Данная валюта отсутствует в списке актуальных. Проверьте вводимое значение.')

    # С конвертируемой валютой проводим те же действия: приводим к верхнему регистру, убираем кавычки и разделяем.
    target_currency = input(f'Введите валюту, на которую хотите обменять: {keys_string}.\n')
    target_currency_up = target_currency.upper()
    if target_currency_up not in exchange_rates:
        return print('Данная валюта отсутствует в списке актуальных. Проверьте вводимое значение.')

    # Проверяем значение количества валюты на отрицательное.
    currency_amount = float(input('Введите количество валюты\n'))
    if currency_amount < 0:
        return print(f'Вы ввели отрицательное значение транзакции.')
    # Этот кусок остался без изменений.
    cross_course = exchange_rates[base_currency] / exchange_rates[target_currency]
    result = round(cross_course * currency_amount, 2)
    # Добавляем название валюты, которую мы хотим приобрести.
    print(result, target_currency_up)


main()

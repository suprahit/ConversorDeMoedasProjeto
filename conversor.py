import requests
from list import list_data_fetch


def conversor_data_fetch(url, from_currency, to_currency, amount):
    data = requests.get("{}/latest?amount={}&from={}&to={}".format(url, amount, from_currency, to_currency))
    data_json = data.json()
    return data_json


def currency_conversor_menu(url):
    data_list_dict = list_data_fetch(url)
    while True:
        try:
            from_currency = input("Type the currency you want to convert from: ").upper()
            to_currency = input("Type the currency you want to convert to: ").upper()
            amount = float(input("Type the amount you want to convert: "))

            if from_currency in data_list_dict and to_currency in data_list_dict and amount >= 0.0:
                data_dict = conversor_data_fetch(url, from_currency, to_currency, amount)
                print("{0} {1} is {2} {3}"
                      .format(amount, from_currency, data_dict["rates"][to_currency], to_currency))
                print("Date: {}".format(data_dict["date"]))
                while True:
                    print("1 - Another conversion")
                    print("2 - Back")
                    try:
                        option = int(input(">>> "))
                        if option == 1:
                            break
                        elif option == 2:
                            return
                        else:
                            raise ValueError
                    except ValueError:
                        print("Choose a valid option!")
                        print("")
            else:
                raise ValueError
        except ValueError:
            print("Type a valid option!")
            print("")

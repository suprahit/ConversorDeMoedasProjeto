import requests


def list_data_fetch(url):
    data = requests.get('{}/currencies'.format(url))
    data_json = data.json()
    return data_json


def currency_list_menu(url):
    data_dict = list_data_fetch(url)
    for key, value in data_dict.items():
        print("{} - {}".format(key, value))
    while True:
        print("")
        print("1 - Back")
        try:
            option = int(input(">>> "))
            if option == 1:
                return
            else:
                raise ValueError
        except ValueError:
            print("Choose a valid option!")
            print("")

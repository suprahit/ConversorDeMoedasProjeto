import requests


def currency_list(url):
    data = requests.get('{}/currencies'.format(url))
    data_dict = data.json()

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

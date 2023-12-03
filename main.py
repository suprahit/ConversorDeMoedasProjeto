from sys import exit
from list import currency_list

url = "https://api.frankfurter.app"

print("")
print("Welcome to the currency converter")
print("Note: Values may change overtime")


def end_app():
    print("Bye bye :)")
    exit(0)


def menu():
    while True:
        print("Choose one option: ")
        print("1 - Currency List")
        print("2 - Currency Converter")
        print("3 - End the app")
        try:
            option = int(input(">>> "))
            if option == 1:
                currency_list(url)
            elif option == 2:
                pass
            elif option == 3:
                end_app()
            else:
                raise ValueError
        except ValueError:
            print("Choose a valid option!")
            print("")


menu()

from sys import exit
from list import currency_list_menu
from conversor import currency_conversor_menu

url = "https://api.frankfurter.app"

print("")
print("Welcome to the currency converter")
print("Note: Values may change overtime")


def menu():
    while True:
        print("Choose one option: ")
        print("1 - Currency List")
        print("2 - Currency Converter")
        print("3 - End the app")
        try:
            option = int(input(">>> "))
            if option == 1:
                currency_list_menu(url)
            elif option == 2:
                currency_conversor_menu(url)
            elif option == 3:
                print("Ending app...")
                exit(0)
            else:
                raise ValueError
        except ValueError:
            print("Choose a valid option!")
            print("")


menu()

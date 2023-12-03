from sys import exit

print("Welcome to the currency converter")
print("Note: Values may change overtime")


def currency_list():
    print("EUR - EURO")
    print("USD - US Dollar")
    print("JPY - Japanese Yen")
    print("BGN - Bulgarian Lev")
    print("CZK - Czech Republic Koruna")
    print("DKK - Danish Krone")
    print("GBP - British Pound Sterling")
    print("HUF - Hungarian Forint")
    print("PLN - Polish Zloty")
    print("RON - Romanian Leu")
    print("SEK - Swedish Krona")
    print("CHF - Swiss Franc")
    print("ISK - Icelandic Króna")
    print("NOK - Norwegian Krone")
    print("HRK - Croatian Kuna")
    print("RUB - Russian Ruble")
    print("TRY - Turkish Lira")
    print("AUD - Australian Dollar")
    print("BRL - Brazilian Real")
    print("CAD - Canadian Dollar")
    print("CNY - Chinese Yuan")
    print("HKD - Hong Kong Dollar")
    print("IDR - Indonesian Rupiah")
    print("ILS - Israeli New Sheqel")
    print("INR - Indian Rupee")
    print("KRW - South Korean Won")
    print("MXN - Mexican Peso")
    print("MYR - Malaysian Riggit")
    print("NZD - New Zealand Dollar")
    print("PHP - Philippine Peso")
    print("SGD - Singapore Dollar")
    print("THB - Thai Baht")
    print("ZAR - South African Rand")
    print("")
    while True:
        print("1 - Back")
        try:
            escolha = int(input(">>> "))
            if escolha == 1:
                return
            else:
                raise TypeError
        except TypeError:
            print("Choose a valid option!")
            print("")



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
            escolha = int(input(">>> "))
            if escolha == 1:
                currency_list()
            elif escolha == 2:
                pass
            elif escolha == 3:
                end_app()
            else:
                raise TypeError
        except TypeError:
            print("Choose a valid option!")
            print("")


menu()

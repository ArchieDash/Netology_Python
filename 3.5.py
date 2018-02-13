import osa
import re


def convert_temp(x):
    client = osa.Client("http://www.webservicex.net/ConvertTemperature.asmx?WSDL")
    return client.service.ConvertTemp(x, FromUnit="degreeFahrenheit", ToUnit="degreeCelsius")


def convert_curr(data):
    client = osa.Client("http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL")
    return client.service.ConvertToNum(fromCurrency=f"{data[2]}", toCurrency="rub", amount=f"{data[1]}", rounding="1")


def convert_length(length):
    client = osa.Client("http://www.webservicex.net/length.asmx?WSDL")
    return client.service.ChangeLengthUnit(LengthValue=f"{length}", fromLengthUnit="Miles", toLengthUnit="Kilometers")


def currencies(file):
    total = list()
    with open(file, "r") as file:
        for line in file:
            data = line.split()
            result = convert_curr(data)
            total.append(result)
    print(f"Total travel cost: {round(sum(total))} RUB")


def length(file):
    total = list()
    with open(file, "r") as file:
        for line in file:
            data = line.split()
            length = data[1].replace(",","")
            result = convert_length(length)
            total.append(result)
        print(f"Total distance: {round(sum(total), 2)} Km")


def avg_temp(file):
    with open(file, "r") as f:
        data = f.read()
        temps = [int(n) for n in re.findall('(\d+)', data)]
        avg_temp = round((sum(temps) / len(temps)), 2)
    print(f"Average temperature {round(convert_temp(avg_temp), 2)} C")


def main():
    while True:
        console = input("1 - Average temperature\n2 - Total travel cost\n3 - Total travel distance\nQ - for quit")
        if console == "1":
            avg_temp("temps.txt")
        elif console == "2":
            currencies("currencies.txt")
        elif console == "3":
            length("travel.txt")
        elif console.lower() == "q":
            break


main()
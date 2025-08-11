def main():
    print("Welcome to the Mexican Peso Currency Converter!")
    print()

    dollars = eval(input("Enter the amount in US Dollars:"))

    peso = convert_to_peso(dollars)

    print("That's", peso, "Mexican Pesos.")

convert_to_peso = lambda dollars: dollars * 18.68
main()
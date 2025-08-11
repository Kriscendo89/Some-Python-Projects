def main():
    print("Welcome to the Brazilian Real Currency Converter!")
    print()

    dollars = eval(input("Enter the amount in US Dollars:"))

    real = convert_to_real(dollars)

    print("That's", real, "Brazilian Reals.")

convert_to_real = lambda dollars: dollars * 5.44
main()
def main():
    print("Welcome to the Australian Dollar Currency Converter!")
    print()

    dollars = eval(input("Enter the amount in US Dollars:"))

    australian_dollar = convert_to_australian_dollar(dollars)

    print("That's", australian_dollar, "Australian dollars.")

convert_to_australian_dollar = lambda dollars: dollars * 1.54
main()
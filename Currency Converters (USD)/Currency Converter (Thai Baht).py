def main():
    print("Welcome to the Thai Baht Currency Converter!")
    print()

    dollars = eval(input("Enter the amount in US Dollars:"))

    baht = convert_to_baht(dollars)

    print("That's", baht, "Thai Bahts.")

convert_to_baht = lambda dollars: dollars * 32.33

main()
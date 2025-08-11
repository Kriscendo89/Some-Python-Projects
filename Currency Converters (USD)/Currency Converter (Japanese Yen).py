def main():
    print("Welcome to the Japanese Yen Currency Converter!")
    print()

    dollars = eval(input("Enter the amount in US Dollars:"))

    yen = convert_to_yen(dollars)

    print("That's", yen, "Japanese Yen.")

convert_to_yen = lambda dollars: dollars * 148.25
main()
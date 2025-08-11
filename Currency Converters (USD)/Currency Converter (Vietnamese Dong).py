def main():
    print("Welcome to the Vietnamese Dong Currency Converter!")
    print()

    dollars = eval(input("Enter the amount in US Dollars:"))

    dong = convert_to_dong(dollars)

    print("That's", dong, "Vietnamese Dong.")

convert_to_dong = lambda dollars: dollars * 26233.02
main()
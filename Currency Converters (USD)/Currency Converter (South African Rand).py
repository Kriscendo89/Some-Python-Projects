def main():
    print("Welcome to the South African Rand Currency Converter!")
    print()

    dollars = eval(input("Enter the amount in US Dollars:"))

    rand = convert_to_rand(dollars)

    print("That's", rand, "South African Rands.")

convert_to_rand = lambda dollars: dollars * 17.77
main()
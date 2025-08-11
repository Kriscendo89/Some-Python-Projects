def main():
    print("Welcome to the Indian Rupee Currency Converter!")
    print()

    dollars = eval(input("Enter the amount in US Dollars:"))

    rupee = convert_to_rupee(dollars)

    print("That's", rupee, "Indian Rupees.")

convert_to_rupee = lambda dollars: dollars * 87.66
main()
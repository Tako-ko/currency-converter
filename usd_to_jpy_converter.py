# This program will ask the user to input a value in either USD or JPY, then it will provide the user with the total value of the conversion.
# First, the program greets the user, prompting them to select whether to convert from USD to JPY, or vice-versa.
print("Hello! Welcome to USD to JPY converter.\nTo start, please first select the currency to convert from.\n Options :\n USD | JPY ")

# The program receives the user's input for the currency choice. The .upper method is called so the choice is case-insensitive
initial_currency = input().upper()
# The program checks if the user input one of the two valid options, asking for a different input if invalid.
while (initial_currency != "USD") and (initial_currency != "JPY"):
    print("Sorry, the received value is not an option.\nplease input a valid option\n USD | JPY")
    initial_currency = input().upper()


def ask_for_amount():
    """Prompt the user for a numerical value to convert and validate it.

    Loops continuously until the user inputs a valid, non-zero positive number.
    Returns the validated amount as a float.
    """
    while True:
        try:
            initial_value = float(input())
            # The inequality checks that the input value is a non-zero positive
            if initial_value <= 0:
                print("Sorry, the input value must be a positive non-zero number, please input a valid value:")
                continue
            break
        except ValueError:
            print("Sorry, the input value must be a number, please input a valid value:")
    return initial_value

if initial_currency == "USD":
    final_currency = "JPY"
    print("Please input the amount to be converted to JPY: ")
    initial_value = ask_for_amount()
    final_value = initial_value * 158.22  # So far, the conversions use a fixed value picked on October 21, 2026

# If the initial currency selected is not USD, the branch converts JPY to USD
else:
    final_currency = "USD"
    print("Please input the amount to be converted to USD: ")
    initial_value = ask_for_amount()
    final_value = initial_value / 158.22  # So far, the conversions use a fixed value picked on October 21, 2026

# After running the calculations, the program will now present the user with their desired total.
print(f"{initial_value:.{2}f} {initial_currency} is equivalent to {final_value:.{2}f} {final_currency}. \nThank you for using USD to JPY converter.")


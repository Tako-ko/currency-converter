# This program will ask the user to input a value in either USD or JPY, then it will provide the user with the total value of the conversion.

# First, the program greets the user, prompting them to select whether to convert from USD to JPY, or vice-versa.

print("Hello! Welcome to USD to JPY converter.\nTo start, please first select the currency to convert from.\n Options :\n USD | JPY ")

# The program will check whether the user input a valid value, if so, it will proceed to the next step, otherwise, the user will be prompted to input a valid value.

initialCurrency = input().upper()
finalCurrency = ""
while (initialCurrency != "USD") and (initialCurrency != "JPY"):
    print("Sorry, the received value is not an option.\nplease input a valid option\n USD | JPY")
    initialCurrency = input().upper()

# The program will ask for the initial value, then run the according calculations given the currency chosen by the user.
# For now, the currency conversion is based on a fixed value.

if initialCurrency == "USD":
    finalCurrency = "JPY"
    print("Please input the amount to be converted to JPY: ")

# The try command under the while loop makes sure the user inputs a numerical value, asking for a different input instead of crashing the program if the value is invalid.
# Likewise, the inequality inside the "if" branch ensures the given value is a non-zero positive.

    while True: 
        try:
            initialValue = float(input())
            if initialValue <= 0:
                print("Sorry, the input value must be a positive non-zero number, please input a valid value:")
                continue
            break
        except ValueError:
            print("Sorry, the input value must be a number, please input a valid value:")

    finalValue = initialValue * 158.22 

# If the initial currency selected is not USD, then the "else" branch below will execute the same process as above, but converting JPY to USD instead.

else:
    finalCurrency = "USD"
    print("Please input the amount to be converted to USD: ")

    while True: 
        try:
            initialValue = float(input())
            if initialValue <= 0:
                print("Sorry, the input value must be a positive non-zero number, please input a valid value:")
                continue
            break
        except ValueError:
            print("Sorry, the input value must be a number, please input a valid value:")
    finalValue = initialValue / 158.22 

#After running the calculations, the program will now present the user with their desired total.

print(f"{initialValue:.{2}f} {initialCurrency} is equivalent to {finalValue:.{2}f} {finalCurrency}. \nThank you for using USD to JPY converter.") 


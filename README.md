# currency-converter
The program will convert from USD to JPY or vice-versa as indicated by the user.

## Example run:

```
Hello! Welcome to USD to JPY converter.
To start, please first select the currency to convert from.
 Options :
 USD | JPY
USD
Please input the amount to be converted to JPY: 
100
100.00 USD is equivalent to 15822.00 JPY. 
Thank you for using USD to JPY converter.
```
## Features:

- Capable of performing two-way conversions.
- Case-insensitive currency choice.
- Checks for invalid or non-positive inputs to prevent crashes and errors.

## Requirements:

- Tested on Python 3.13.2.
- Tested on Windows 11.
- No external packages needed.

## How to run:

**Step 1: Get the project onto your computer. Pick one**

   **Option A: with Git**
```
git clone https://github.com/Tako-ko/currency-converter.git
```
   **Option B: without Git**
   
   On the GitHub page, click the green **Code** button, then **Download ZIP**, and unzip it.

**Step 2: Open a terminal and move into the project folder**
```
cd currency-converter
```

**Step 3: Run the program**
```
python usd_to_jpy_converter.py
```

**Step 4: Follow the prompts: choose USD or JPY, then enter an amount**

## Known limitations:

- Leading space input is read as an invalid option.
- `nan` and `inf` values will result in illogical conversions.
- The rate is currently fixed at 158.22 (Picked on October 21, 2026).

## Roadmap:

- [x] Hardcoded USD to JPY.
- [x] Bidirectional conversion.
- [x] try/except code to prevent errors.
- [ ] Fix `nan` / `inf`.
- [ ] Fix leading space currency.
- [ ] Rates dictionary.
- [ ] More currency options.
- [ ] Live exchange rates from API.
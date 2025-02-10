def hex_to_decimal(hex_num):

    decimal_value = 0
    hex_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    hex_num = hex_num.upper()

    for i, digit in enumerate(reversed(hex_num)):
        if digit not in hex_map:
            raise ValueError(f"Invalid character {digit} in hexadecimal number")
        decimal_value += hex_map[digit] * (16 ** i)

    return decimal_value


def decimal_to_hex(decimal_num):
    if decimal_num == 0:
        return "0"
    
    hex_digits = "0123456789ABCDEF"
    
    hex_num = ""
    
    while decimal_num > 0:
        remainder = decimal_num % 16
        hex_num = hex_digits[remainder] + hex_num
        decimal_num = decimal_num // 16
    
    return hex_num


def main():
    print("Welcome to the base conversion program!")
    print("Choose an option:")
    print("1. Convert from Hexadecimal (base 16) to Decimal (base 10)")
    print("2. Convert from Decimal (base 10) to Hexadecimal (base 16)\n")

    option = input("Enter 1 or 2: ")

    if option == '1':
        hex_input = input("Enter a hexadecimal number (e.g., A3F): ").strip()
        try:
            result = hex_to_decimal(hex_input)
            print(f"The decimal value of {hex_input} is {result}")
        except ValueError as e:
            print(f"Error: {e}")
    
    elif option == '2':
        dec_input = input("Enter a decimal number: ").strip()
        try:
            dec_input = int(dec_input)  # Ensure it's a valid integer
            result = decimal_to_hex(dec_input)
            print(f"The hexadecimal value of {dec_input} is {result}")
        except ValueError:
            print("Error: Please enter a valid integer for the decimal number.")
    
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()

# Debugged this code

def validate_isbn(isbn, length):
    # Length validation
    if len(isbn) != length:
        print(f"ISBN-{length} code should be {length} digits long.")
        return

    main_digits = isbn[:-1]
    given_check_digit = isbn[-1]

    # Validate characters based on length
    if length == 10:
        # first 9 must be digits
        if not main_digits.isdigit():
            print("Invalid character was found.")
            return

        # last digit can be 0-9 or X
        if not (given_check_digit.isdigit() or given_check_digit == "X"):
            print("Invalid character was found.")
            return

        main_digits_list = [int(d) for d in main_digits]
        expected_check_digit = calculate_check_digit_10(main_digits_list)

    else:  # length == 13
        # all must be digits
        if not isbn.isdigit():
            print("Invalid character was found.")
            return

        main_digits_list = [int(d) for d in main_digits]
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # Final validation
    if given_check_digit == expected_check_digit:
        print("Valid ISBN Code.")
    else:
        print("Invalid ISBN Code.")


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        return "0"
    elif result == 10:
        return "X"
    else:
        return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10

    if result == 10:
        return "0"
    else:
        return str(result)


def main():
    user_input = input("Enter ISBN and length: ")

    # Must be comma separated
    if "," not in user_input:
        print("Enter comma-separated values.")
        return

    values = user_input.split(",")

    # Must be exactly 2 values: isbn,length
    if len(values) != 2:
        print("Enter comma-separated values.")
        return

    isbn = values[0].strip()
    length_str = values[1].strip()

    # Length must be numeric
    if not length_str.isdigit():
        print("Length must be a number.")
        return

    length = int(length_str)

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print("Length should be 10 or 13.")


# main()

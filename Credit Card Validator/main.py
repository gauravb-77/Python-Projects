# Python credit card validator program

# 1. Remove any '-' or ' ' 
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left
#       (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 and 3
# 5. If sum is divisible by 10, the credit card number is valid

def is_credit_card_number_valid(credit_card_number):
    credit_card_number = credit_card_number[::-1]
    credit_card_number = credit_card_number.replace('-', '').replace(' ', '')

    odd_digits_sum = 0
    even_digits_sum = 0

    for x in credit_card_number[::2]:
        odd_digits_sum += int(x)

    for x in credit_card_number[1::2]:
        x = int(x) * 2
        if x >= 10:
            even_digits_sum += (1 + (x % 10))
        else:
            even_digits_sum += x

    total = odd_digits_sum + even_digits_sum

    return total % 10 == 0


def main():
    credit_card_number = input("Enter credit card number: ")

    if is_credit_card_number_valid(credit_card_number):
        print("VALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
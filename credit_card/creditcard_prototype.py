
from tokenize import String

from collection.creditCard import convert_to_array, validate_length, sum_array_last, sum_array_second_to_last, \
    get_card_type
from collection.test_creditCard import TestCreditCard

print("App to validate CreditCard")
credit_card_number = str(input("Enter credit card number: "))
while not validate_length(credit_card_number) and not String.isdigit():
    print("Invalid credit card number")
    credit_card_number = str(input("Enter credit card number: "))


card_type = get_card_type(credit_card_number)
arr = convert_to_array(credit_card_number)
sum_array = sum_array_last(arr)
sum_array_second = sum_array_second_to_last(arr)
total_sum = sum_array + sum_array_second
validate = False
if total_sum % 10 == 0:
    validate = True
validity_status: str = "Valid" if validate else "Invalid"

print(f'''
****Credit Card Type: {card_type},
****Credit Card Number: {credit_card_number},
****Credit Card Digit Length: {len(credit_card_number)},
****Credit Card Validity Status: {validity_status}
''')

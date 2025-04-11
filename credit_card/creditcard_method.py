def convert_to_array( input):
    array = []
    for number in input:
        array.append(int(number))
    return array

def validate_length(input):
    if len(input) < 13 or len(input) > 16:
        return False
    return True

def sum_array_last( input):
    sum = 0
    counter = len(input) - 1
    while counter >= 0:
        sum += input[counter]
        counter -= 2
    return sum

def sum_array_second_to_last( input):
    sum = 0
    counter = len(input) - 2
    while counter >= 0:
        temp = input[counter] * 2
        if temp > 9:
            temp -= 9
        sum += temp
        counter -= 2
    return sum

def get_card_type(input):
    if input[0] == '4':
        return "Visa"
    elif input[0] == '5':
        return "MasterCard"
    elif input[0] == '6':
        return "Discover Card"
    elif input[0] == '3' and input[1] == '7':
        return "Amex"
    return "Unknown"






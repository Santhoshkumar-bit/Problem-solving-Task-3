##First and last digit of integer
def sum_first_last_digit(number):

    number_str = str(number)
    

    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])
    
   
    sum_digits = first_digit + last_digit
    
    return sum_digits

number = 23426347
result = sum_first_last_digit(number)
print("Sum of first and last digit:", result)
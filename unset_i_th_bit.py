def unset_bit(num1: int, bit: int) -> int:
    m = 1 << bit
    if num1 & m:
        num1 = num1 & ~m
    return num1


try:
    number1 = int(input("Enter an integer : "))
    number2 = int(input("Enter bit to change : "))
    print("The updated value is : ", unset_bit(number1, number2))
except ValueError:
    print("Invalid input. Please enter only integers")

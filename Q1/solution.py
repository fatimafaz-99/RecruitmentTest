def get_factorial(number):
    factorial_result = 1
    for i in range(1, (number + 1)):
        factorial_result = i * factorial_result
    return factorial_result


def sum_of_digits(number):
    factorial_sum = 0
    while (number != 0):
        factorial_sum = factorial_sum + (number % 10)
        number = number // 10
    return factorial_sum



def main():
    input_val = int(input("Please enter the number: "))
    print(sum_of_digits(get_factorial((input_val))))

if __name__ == "__main__":
    main()

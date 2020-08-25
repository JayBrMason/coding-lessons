print("Welcome to the Factorial Calculator!")


def factorial(num):
    while num > 0 and num <= 10:
        if num == 1:
            return 1


        return(num * factorial(num - 1))

    start()


def start():
    num = int(input("Enter a whole number that’s greater than 0 but less than 10\n"))
    print(f"The factorial of {str(num)} is {str(factorial(num))}.")

    run_again = input('Continue? ')
    print(run_again)
    run_again = run_again.lower()

    if run_again == 'y':
        start()
    else:
        print('Goodbye!')
        exit() 


start() 

factorial(num)
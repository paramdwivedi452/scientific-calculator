import math
import cmath
import statistics


def show_menu():
    print("\n--- Scientific Calculator ---")
    print("1. Basic calculation (+, -, *, /)")
    print("2. Power")
    print("3. Square root")
    print("4. Trigonometry (sin, cos, tan)")
    print("5. Logarithm")
    print("6. Mean and median")
    print("7. Complex number square root")
    print("0. Exit")


def basic_calculation():
    first = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    second = float(input("Enter the second number: "))

    if operator == "+":
        answer = first + second
    elif operator == "-":
        answer = first - second
    elif operator == "*":
        answer = first * second
    elif operator == "/":
        if second == 0:
            print("Cannot divide by zero.")
            return
        answer = first / second
    else:
        print("Invalid operator.")
        return

    print("Answer:", answer)


def trigonometry():
    angle = float(input("Enter the angle in degrees: "))
    function = input("Choose a function (sin, cos, tan): ").lower()

    #python use radian
    radians = math.radians(angle)

    if function == "sin":
        answer = math.sin(radians)
    elif function == "cos":
        answer = math.cos(radians)
    elif function == "tan":
        answer = math.tan(radians)
    else:
        print("Please choose sin, cos, or tan.")
        return

    print("Answer:", round(answer, 6))


def logarithm():
    number = float(input("Enter a number: "))
    base = input("Choose a base (10 or e): ").lower()

    if number <= 0:
        print("The number must be greater than zero.")
    elif base == "10":
        print("Answer:", math.log10(number))
    elif base == "e":
        print("Answer:", math.log(number))
    else:
        print("Please enter 10 or e as the base.")


def statistics_calculation():
    values = input("Enter numbers separated by commas: ")
    numbers = [float(value.strip()) for value in values.split(",")]

    print("Mean:", statistics.mean(numbers))
    print("Median:", statistics.median(numbers))


def main():
    while True:
        show_menu()
        choice = input("Choose an option from above as number(ex=1,2,3..): ")

        try:
            if choice == "1":
                basic_calculation()
            elif choice == "2":
                number = float(input("Enter a number: "))
                power = float(input("Enter the power: "))
                print("Answer:", math.pow(number, power))
            elif choice == "3":
                number = float(input("enter an number: "))
                if number < 0:
                    print("A negative number does not have a real square root")
                else:
                    print("Answer:", math.sqrt(number))
            elif choice == "4":
                trigonometry()
            elif choice == "5":
                logarithm()
            elif choice == "6":
                statistics_calculation()
            elif choice == "7":
                number = complex(input("Enter a complex number, such as 3+4j: "))
                print("Square root:", cmath.sqrt(number))
            elif choice == "0":
                print("Calculator closed. Goodbye!")
                break
            else:
                print("Please choose an option from the menu.")

        except ValueError:
            print("Invalid input. Please try again.")
        except OverflowError:
            print("The result is too large to calculate.")


if __name__ == "__main__":
    main()

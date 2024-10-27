class SimpleCalculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

    def power(self, x, y):
        return x ** y

    def square_root(self, x):
        if x < 0:
            return "Error! Cannot compute the square root of a negative number."
        return x ** 0.5

def main():
    calculator = SimpleCalculator()
    print("Welcome to the Simple Calculator!")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {calculator.power(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter a number: "))
            print(f"Square root of {num} = {calculator.square_root(num)}")
        
        else:
            print("Invalid input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

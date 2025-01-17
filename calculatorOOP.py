class SimpleCalculator:
    def __init__(self):
        print("Hi! Welcome to the Simple Calculator!")
        print("Here you can perform basic operations like addition, subtraction, multiplication, and division.")

    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero is undefined."
        else:
            return a / b
        
    def run(self):
        while True:
            print("\nSelect operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Exit")

            choice = input("Enter choice (1/2/3/4/5): ")

            if choice == "5": 
                print("Thank you for using the Simple Calculator. Goodbye!")
                break

            if choice in ["1", "2", "3", "4"]:
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                    continue

                if choice == "1":
                    print(f"Result: {self.add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {self.subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {self.multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Result: {self.divide(num1, num2)}")

            else:
                print("Invalid choice. Please select a valid operation.")

if __name__=="__main__":
    calculator = SimpleCalculator()
    calculator.run()
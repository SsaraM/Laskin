def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def modulo(x, y):
    return x % y

print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulo") #vaihtoehdot

while True:
    choice = input("Select operation: ") #valitse vaihtoehdoista

    if choice in ('1', '2', '3', '4', '5'): 
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", modulo(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ") #uusi lasku
        if next_calculation == "no":
            break
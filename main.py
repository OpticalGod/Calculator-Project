from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

math_dic = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# result = math_dic["*"](4,8)
result = 0
go_again = ""
operator = ""
print(logo)
while go_again != "stop":
    if go_again == "y":
        n1 = result
        operator = input("Enter the operator '+', '-', '*' or '/':\n")
        n2 = float(input("Enter the second number:\n"))
    elif go_again == "n" or go_again == "":
        n1 = float(input("Enter the first number:\n"))
        operator = input("Enter the operator '+', '-', '*' or '/':\n")
        n2 = float(input("Enter the second number:\n"))
    if operator == "+":
        result = math_dic["+"](n1, n2)
    elif operator == "-":
        result = math_dic["-"](n1, n2)
    elif operator == "*":
        result = math_dic["*"](n1, n2)
    elif operator == "/":
        result = math_dic["/"](n1, n2)
    else:
        print("Invalid operator")
    print(f"Final answer is {n1} {operator} {n2} = {result}")
    go_again = input(f"If you want to continue with the '{result}' type 'Y'\n"
                     f"If you want to start again type 'N'\n"
                     f"To end the program type 'Stop'\n").lower()

import art

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {"+": add, "-": sub, "*": mul, "/": div}
continueCalc = True
newCalc = True
while newCalc:
    print(art.logo)
    num1 = round(float(input("What's the first number...:\n")), 1)
    while continueCalc:
        operator = input("+\n-\n*\n/\nPick an operation...:\n")
        num2 = round(float(input("What's the next number...:\n")), 1)
        result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
        aux = input(f"type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if aux == 'n':
            continueCalc = False
        num1 = result
    
    continueCalc = True
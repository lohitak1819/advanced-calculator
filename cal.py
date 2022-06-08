import math
print("Enter simple for simple calculator and advanced for advanced calculator")

calculator_type = str(input())

if calculator_type == "simple":
    print("Enter the first number")
    a = int(input())
    print("Enter the second number")
    b = int(input())
    print("Enter the operator")
    operator = input()
    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    elif operator == "*":
        print(a * b)
    else:
        print(a/b)

else:
    print("Enter the nmber")
    num = int(input())
    print("Enter the operator square root or square")
    advanced_operator = input()
    if advanced_operator == "square root":
        print(math.sqrt(num))
    else:
        print(num*num)



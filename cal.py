import math
print("Do you want area calculator or area calculator")
var1 = input()

if var1 == "calculator":
    print("Enter simple for simple calculator or advanced for advanced calculator")
    calculator_type = input()
    if calculator_type == "simple":
        print("Enter operator")
        operator = input()
        print("Enter the first number")
        a = int(input())
        print("Enter the second number")
        b = int(input())
        if operator == "+":
            print(a + b)
        elif operator == "-":
            print(a - b)
        elif operator == "*":
            print(a*b)
        else:
            print(a/b)
    else:
        print("Enter square root,square,cube root or cube")
        o = input()
        print("Enter the number")
        x = int(input())
        if o == "square root":
            print(math.sqrt(x))
        elif o == "cube":
            print(x*x*x)
        elif o == "square":
            print(x*x)
        elif o == "cube root":
            print(x **(1./3.))

else:
    print("Enter the shape")
    shape = input()
    if shape == "square":
        print("What is the side of square")
        side_square = int(input())
        print("The area of the square is")
        print(side_square*side_square)
    elif shape == "triangle":
        print("Enter height of the triangle")
        height_triangle = int(input())
        print("Enter the length of base")
        base_triangle = int(input())
        print(1/2*height_triangle*base_triangle)
    else:
        print("Enter the breadth of the rectangle")
        breadth_rectangle = int(input())
        print("Enter the length of the rectangle")
        length_rectangle = int(input())
        print(breadth_rectangle*length_rectangle)

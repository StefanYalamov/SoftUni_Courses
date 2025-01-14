from math import pi

figure = input("square, rectangle, circle, triangle: ")

if figure == "square":
    a = float(input())
    square_figure = a * a
    print(round(square_figure, 3))

if figure == "rectangle":
    a = float(input())
    b = float(input())
    rectangle_figure = a * b
    print(round(rectangle_figure, 3))

if figure == "circle":
    r = float(input())
    circle_figure = (r * r) * pi
    print(round(circle_figure, 3))

if figure == "triangle":
    a = float(input())
    ha = float(input())
    triangle_figure = (a * ha) / 2
    print(round(triangle_figure, 3))

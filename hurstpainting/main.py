# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# print(colors)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, b, g)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
import random

color_list = [(237, 96, 230), (13, 170, 115), (166, 46, 79), (188, 63, 12), (213, 87, 157), (129, 203, 181),
              (234, 46, 76), (33, 83, 139), (5, 91, 34), (146, 35, 167), (76, 21, 40), (110, 165, 187), (167, 91, 47),
              (227, 147, 117), (14, 212, 170), (59, 89, 160), (6, 51, 95), (219, 119, 71), (95, 69, 21),
              (240, 190, 162), (147, 224, 205), (12, 106, 87), (211, 10, 222), (248, 145, 170), (9, 127, 45),
              (7, 41, 75)]

tim = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
turtle.setworldcoordinates(-370, -370, 370, 370)
tim.pu()
x_coord = -350
y_coord = -350
num_row = 10
tim.setx(x_coord)
tim.sety(y_coord)


def draw_dot():
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

for num in range(num_row):
    tim.setx(x_coord)
    tim.sety(y_coord)
    for num in range(num_row):
        draw_dot()
    y_coord += 60


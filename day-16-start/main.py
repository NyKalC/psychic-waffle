# from turtle import Turtle, Screen
#
# johnny = Turtle()
# johnny.shape("turtle")
# johnny.color("DarkGreen")
# johnny.forward(100)
#
#
#
# my_screen = Screen()
# my_screen.canvheight
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Names", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table)
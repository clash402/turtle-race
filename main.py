from turtle import Turtle, Screen
import random


# PROPERTIES
screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
random.shuffle(colors)

turtles = []
pos_y = -145

for color in colors:
    turtle = Turtle("turtle")
    turtle.shapesize(2)
    turtle.color(color)
    turtle.penup()
    turtle.goto(-210, pos_y)
    turtles.append(turtle)
    pos_y += 60


# METHODS
def turtle_crossed_finish_line(current_turtle):
    if current_turtle.xcor() > 210:
        return True


def determine_winner():
    if winning_color == user_color:
        print(f"You won! The {winning_color} turtle won.")
    else:
        print(f"You lost. The {winning_color} turtle won.")


# MAIN
user_color = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ").lower()
race_is_in_progress = True

while race_is_in_progress:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))

        if turtle_crossed_finish_line(turtle):
            race_is_in_progress = False
            winning_color = turtle.pencolor()

            determine_winner()

screen.exitonclick()

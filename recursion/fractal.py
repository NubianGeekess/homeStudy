import turtle

def main():
    wn = turtle.Screen()  # creates a graphics window
    alex = turtle.Turtle()  # create a turtle named alex
    alex.forward(150)  # tell alex to move forward by 150 units
    alex.left(90)  # turn by 90 degrees
    alex.forward(75)  # complete the second side of a rectangle
    turtle.exitonclick()
if __name__ == "__main__":
    main()
import turtle

def main(t, order, size):
    """
    Make a turtle t draw a koch fractal of order and size Leave the turtle facing the same direction
    :param t:
    :param order:
    :param size:
    :return:
    """
    wn = turtle.Screen()
    t = turtle.Turtle()

    if order == 0:
        t.forward(size)
    else:
        main(t, order-1, size/3)  # Go 1/3 of the way
        t.left(60)
        main(t, order-1, size/3)
        t.right(120)
        main(t, order - 1, size / 3)
        t.right(60)
        main(t, order - 1, size / 3)

if __name__ == "__main__":
    main(1, 10, 70)

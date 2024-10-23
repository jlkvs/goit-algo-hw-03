import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def draw_snowflake(order):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.color("blue")

    for _ in range(3):
        koch_snowflake(t, order, 300)  
        t.right(120)
  
    t.hideturtle()
    window.exitonclick()

try:
    level = int(input("Введіть рівень рекурсії (не менше 0): "))
    if level < 0:
        print("Рівень рекурсії має бути не менше 0.")
    else:
        draw_snowflake(level)
except ValueError:
    print("Будь ласка, введіть ціле число.")

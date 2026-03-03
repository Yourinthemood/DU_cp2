#DU p1 Larose recursion fractal design

'''
Fractal / Sierpenski Triangle and Koch Snowflake Fractal Generator
'''

import turtle

# main function that runs the program
def main():
    # greet the user
    print("=" * 50)
    print("Welcome to the Fractal Generator!")
    print("=" * 50)
    
    # ask which fractal to draw
    print("\nFractal options:")
    print("1. Sierpinski Triangle")
    print("2. Koch Snowflake (I attempted to make it, but it took too long and im tired)")
    fractal_choice = 0
    while fractal_choice < 1 or fractal_choice > 2:
        try:
            fractal_choice = int(input("Choose fractal (1 or 2): "))
            if fractal_choice < 1 or fractal_choice > 2:
                print("Please enter 1 or 2.")
        except ValueError:
            print("Please enter a valid number.")
    
    # get recursion depth from user (1-5)
    depth = 0
    while depth < 1 or depth > 5:
        try:
            depth = int(input("Enter recursion depth (1-5): "))
            if depth < 1 or depth > 5:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")
    
    print()
    color = input("Enter fractal color (e.g., red, blue, green): ")
    
    # ask about background color
    print()
    bg_choice = input("Change background color? (yes/no): ").lower()
    bg_color = "white"
    if bg_choice == "yes":
        bg_color = input("Enter background color: ")
    
    print("\nDrawing your fractal...\n")
    
    # set up the turtle screen
    screen = turtle.Screen()
    screen.bgcolor(bg_color)
    screen.tracer(0)  # Turn off animation for faster drawing
    if fractal_choice == 1:
        screen.title("Sierpinski Triangle")
    else:
        screen.title("Koch Snowflake")
    
    # create and setup turtle
    t = turtle.Turtle()
    t.speed(0)  # fastest speed
    t.color(color)
    t.penup()
    
    # draw based on user choice
    if fractal_choice == 1:
        # Sierpinski Triangle - start from bottom left corner
        t.goto(-300, -250)
        t.pendown()
        draw_sierpinski(t, 600, depth)
    else:
        # Koch Snowflake - start from left side
        t.goto(-300, 100)
        t.pendown()
        # draw three sides of the snowflake
        for i in range(3):
            draw_koch(t, 600, depth)
            t.right(120)
    
    t.hideturtle()
    screen.update()  # Update the screen after drawing
    
    print("Done drawing!\n")
    
    # ask about saving image
    save_choice = input("Save as image? (yes/no): ").lower()
    if save_choice == "yes":
        canvas = screen.getcanvas()
        filename = input("Enter filename (end with .eps): ")
        if not filename.endswith('.eps'):
            filename = filename + '.eps'
        canvas.postscript(file=filename)
        print("Saved as " + filename)
    
    input("Press Enter to exit.")
    screen.bye()

# recursive function to draw sierpinski triangle
def draw_sierpinski(t, length, depth):
    # base case - draw a filled triangle
    if depth == 1:
        t.begin_fill()
        for i in range(3):
            t.forward(length)
            t.left(120)
        t.end_fill()
    else:
        # draw three smaller triangles in the corners
        
        # bottom left triangle
        draw_sierpinski(t, length/2, depth-1)
        
        # move to bottom right position
        t.penup()
        t.forward(length/2)
        t.pendown()
        
        # bottom right triangle
        draw_sierpinski(t, length/2, depth-1)
        
        # move to top position
        t.penup()
        t.backward(length/2)
        t.left(60)
        t.forward(length/2)
        t.right(60)
        t.pendown()
        
        # top triangle
        draw_sierpinski(t, length/2, depth-1)
        
        # return to starting position
        t.penup()
        t.right(60)
        t.backward(length/2)
        t.left(60)
        t.pendown()

main()

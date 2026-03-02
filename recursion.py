#DU p1 Larose recursion fractal design

import turtle

# main function that runs the program
def main():
    # greet the user and get inputs
    print("Welcome to the Sierpinski Triangle Generator")
    print("This program creates a Sierpinski Triangle fractal using recursion.\n")
    
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
    color = input("Enter triangle color (e.g., red, blue, green): ")
    
    # ask about background color (extra credit)
    print()
    bg_choice = input("Change background color? (yes/no): ").lower()
    bg_color = "white"
    if bg_choice == "yes":
        bg_color = input("Enter background color: ")
    
    print("\nGenerating Sierpinski Triangle...\n")
    
    # set up the turtle screen
    screen = turtle.Screen()
    screen.bgcolor(bg_color)
    screen.title("Sierpinski Triangle")
    
    # create and setup turtle
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    t.penup()
    t.goto(-200, -150)
    t.pendown()
    
    # call recursive function
    draw_sierpinski(t, 400, depth)
    t.hideturtle()
    
    print("Fractal generated successfully!\n")
    
    # ask about saving image (extra credit)
    save_choice = input("Save as image? (yes/no): ").lower()
    if save_choice == "yes":
        canvas = screen.getcanvas()
        filename = input("Enter filename (with .eps): ")
        canvas.postscript(file=filename)
        print(f"Saved as {filename}")
    
    input("\nPress Enter to exit the program.")
    screen.bye()

# recursive function to draw sierpinski triangle
def draw_sierpinski(t, length, depth):
    # base case - draw a triangle
    if depth == 0:
        for i in range(3):
            t.forward(length)
            t.left(120)
    else:
        # recursive case - draw three smaller triangles
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
        
        # return to start
        t.penup()
        t.right(60)
        t.backward(length/2)
        t.left(60)
        t.pendown()

main()

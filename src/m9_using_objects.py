"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and Dylan Frazee.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    #two_circles()
    #circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------
    window = rg.RoseWindow(300, 300)
    c1 = rg.Circle(rg.Point(100,100),15)
    c1.fill_color = 'orange'
    c1.attach_to(window)

    c2 = rg.Circle(rg.Point(50,50),25)
    c2.attach_to(window)
    window.render()
    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(400,400)
    x = 100
    y = 100
    circle_center = rg.Point(x,y)
    c = rg.Circle(circle_center,10)
    c.fill_color = 'blue'
    c.outline_thickness = 1
    c.attach_to(window)

    a = 150
    b = 300
    d = (a+b)/2
    r = rg.Rectangle(rg.Point(a,a),rg.Point(b,b))
    r.attach_to(window)

    print(c.outline_thickness)
    print(c.fill_color)
    print(c.center)
    print(x)
    print(y)
    print()
    print(r.outline_thickness)
    print(r.fill_color)
    print('Point(',d,d,')')
    print(d)
    print(d)

    window.render()
    window.close_on_mouse_click()



def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # DONE: 4. Implement and test this function.

    window = rg.RoseWindow(400,400)
    a = 50
    b = 100
    l = rg.Line(rg.Point(a,a),rg.Point(b,b))
    l.thickness = 4
    x = l.get_midpoint()
    l.attach_to(window)

    print(x)
    print((a+b)/2)
    print((a+b)/2)

    p = rg.Line(rg.Point(150,150),rg.Point(300,300))
    p.attach_to(window)

    window.render()
    window.close_on_mouse_click()
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

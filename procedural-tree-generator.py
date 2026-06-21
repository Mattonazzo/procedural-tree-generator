"""
Procedural Tree Generator

A recursive procedural tree generator built with Python's turtle module.
The tree structure is generated using randomized branch lengths,
angles, and probabilities, resulting in a unique tree every run.

Author: Antonazzo Matteo
"""

import turtle
import random
import time

# Window dimensions
WIDTH=1400
HEIGHT=900

# Tree trunk and branch color
BROWN="#5f2b19"

# Initial branch parameters
BRANCH_LEN_START=65
HALF_BRANCH_LEN_START=BRANCH_LEN_START//2

# Maximum random angle variation for branches
BRANCH_ANGLE_VARIATION=20
HALF_BRANCH_ANGLE_VARIATION=BRANCH_ANGLE_VARIATION//2

# Probability of generating a new branch
GENERATION_PROBABILITY=0.7
HALF_GENERATION_PROBABILITY=GENERATION_PROBABILITY/2

def sky(t):
    """
    Draws the sky background.
    """
    t.color("deep sky blue")
    t.fillcolor("deep sky blue")
    t.begin_fill()
    t.right(90)
    t.forward(WIDTH/2)
    t.left(90)
    t.forward(WIDTH/2)
    t.left(90)
    t.forward(WIDTH)
    t.left(90)
    t.forward(WIDTH/2)
    t.left(90)
    t.forward(WIDTH/2)
    t.end_fill()
    # turtle.update()

def tree(branch_len,t):
    """
    Recursively generates a procedural tree using
    random branching angles and branch lengths.
    """

    if branch_len > 6:
        
        # Generate a random branch angle
        branch_angle = random.randint(-BRANCH_ANGLE_VARIATION,  BRANCH_ANGLE_VARIATION)
        
        sign = random.choice((-1, 1))
        branch_angle = sign * random.randint(HALF_BRANCH_ANGLE_VARIATION, BRANCH_ANGLE_VARIATION)
            
        # Scale branch thickness according to branch length
        branch_width = max(1, 2 * (branch_len // 4))
        
        t.down()
        t.width(branch_width if branch_width>HALF_BRANCH_LEN_START-1 else max(1,branch_width-6))
        
        # Switch to leaf color on thin branches
        if branch_width <= 6 and t.pencolor() != "dark green":
                t.color("dark green")
        t.forward(branch_len)
        
        # First recursive branch
        t.right(branch_angle)
        if random.random() < GENERATION_PROBABILITY:
            tree(branch_len - random.randrange(max(branch_width//10,5),max(branch_width//4,8)),t)
            
        # turtle.update()
        
        angle_variation = random.randrange(-BRANCH_ANGLE_VARIATION+1, BRANCH_ANGLE_VARIATION)
        
        # Second recursive branch
        t.left(branch_angle*2+angle_variation)
        
        if random.random() < GENERATION_PROBABILITY:
            tree(branch_len - random.randrange(max(branch_width//10,5),max(branch_width//4,8)),t)
        t.right(branch_angle+angle_variation)
        
        # Additional secondary branches
        angle_variation = random.randrange(-BRANCH_ANGLE_VARIATION+1, BRANCH_ANGLE_VARIATION)
        
        t.right(angle_variation)
        
        if random.random() < HALF_GENERATION_PROBABILITY:
            tree(branch_len - random.randrange(max(branch_width//10,5),max(branch_width//3,8)),t)
        if random.random() < HALF_GENERATION_PROBABILITY:
            tree(branch_len - random.randrange(max(branch_width//10,5),max(branch_width//3,8)),t)
        
        # Small twigs near the branch tip
        for _ in range (3):
            t.left(angle_variation)
            if random.random() < 0.2:
                tree(11 if branch_len>11 else branch_len-1,t)
            t.right(angle_variation)
            if random.random() < 0.2:
                tree(11 if branch_len>11 else branch_len-1,t)
        
        t.left(angle_variation)
        
        # Return to the branch starting point
        t.up()
        if t.pencolor() != BROWN:
            t.color(BROWN)
        t.backward(branch_len)
    else:
        # Terminal node: draw either a leaf or a fruit
        n = random.randrange(0,200)
        if n == 50:
            # make an orange fruit
            t.dot(15, "orange red")
        else:
            # make a leaf 
            t.width(1)
            t.color("dark green")
            t.fillcolor("green")
            t.begin_fill()
            t.circle(10,90)
            t.left(90) #180-90
            t.circle(10,90)
            t.left(90) #90-0
            t.end_fill()

def floor (t):
    """
    Draws the ground beneath the tree.
    """
    
    t.down()
    t.color("green")
    t.width(1)
    t.backward(50)
    t.left(90)
    t.fillcolor("green")
    t.begin_fill()
    t.forward(WIDTH/2)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(WIDTH)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(WIDTH/2)
    t.end_fill()
    t.right(90)
    turtle.update()

def main():
    """
    Creates the scene, generates the tree and
    displays the execution time.
    """

    t = turtle.Turtle()
    turtle.setup(WIDTH,HEIGHT)
    my_win = turtle.Screen()
    t.hideturtle()
    
    # Disable automatic screen updates for better performance
    turtle.tracer(False)

    t.left(90)
    t.up()
    t.backward(300)
    t.down()

    sky(t)

    t.left(90)
    t.color(BROWN)
    start_time = time.perf_counter()
    tree(BRANCH_LEN_START,t)
    end_time = time.perf_counter()
    duration = end_time - start_time

    floor(t)
    
    # Display generation time
    t.penup()
    t.goto(450, 150)
    t.color("dark green")
    t.write(f"Seconds\n{duration:.4f}", align="center", font=("Arial", 68, "normal"))
    
    my_win.exitonclick()

main()


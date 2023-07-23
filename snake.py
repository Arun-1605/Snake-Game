from turtle import Turtle, Screen

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
DISTANCE =20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
            

    def add_segment(self,pos):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(pos)
        self.segments.append(tim)


    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    
    def move(self):
         
         for segment in range(len(self.segments) - 1,0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x,new_y)
         self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    
        

        
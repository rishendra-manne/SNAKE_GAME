from turtle import Turtle,Screen
import time
import random
r=3
START=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in START:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
          seg.goto(1000,1000)
        self.segments.clear()  
        self.create_snake()
        self.head=self.segments[0]  
          
      
       
           
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
           
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)
           
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
   
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
   

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
    def redraw(self):
        xp=random.randint(-280,280)
        yp=random.randint(-280,280)
        self.goto(xp,yp)
   
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
       
        self.hideturtle()
        self.update_turtle()
    def update_turtle(self):
        self.write(f"score:{self.score} Highscore :{self.high_score}",align="center",font=("Arial",21,"normal"))
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        self.update_turtle()
    ##def game_over(self):
      ##  self.goto(0,0)
        ##self.write("GAME OVER",align="center",font=("Arial",21,"normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_turtle()
           
   
   
screen=Screen()
screen.title("snake game")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
s=Snake()
food=Food()
score=Scoreboard()

game_on=True
screen.listen()
screen.onkey(s.up,"Up")
screen.onkey(s.down,"Down")
screen.onkey(s.left,"Left")
screen.onkey(s.right,"Right")

while game_on:
   
    screen.update()
    time.sleep(0.5)
    s.move()
    if s.head.distance(food)<15:
        food.redraw()
        score.increase_score()
        s.extend()
       
    if s.head.xcor()==280 or s.head.xcor()==-280 or s.head.ycor()==280 or s.head.ycor()==-280:
        score.reset()
        
    for seg in s.segments:
        if seg==s.head:
            pass
        elif s.head.distance(seg)<5:
            score.reset()
            

   




screen.exitonclick()

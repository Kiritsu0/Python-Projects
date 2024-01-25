import turtle
wind=turtle.Screen()
wind.title('Ping Pong') #set the title of the window
wind.bgcolor('black') #set the background color of the window
wind.setup(width=800,height=600) #set the width and the height of the window
wind.tracer(0) #stop the windpw from updating automatically

#user1
user1=turtle.Turtle() #initializes turtle object(shape)
user1.speed(0) #set the speed of the animation
user1.shape('square') #set the shape of the object
user1.color('blue') #set the color of the shape
user1.shapesize(stretch_wid=5 , stretch_len=1) #stretches the shape to meet the size
user1.penup() #stops the object from drawing lines
user1.goto(-350,0) #set the position of the object

#user2
user2=turtle.Turtle()
user2.speed(0)
user2.shape('square')
user2.color('red')
user2.shapesize(stretch_wid=5 , stretch_len=1)
user2.penup()
user2.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.x=0.5
ball.y=0.5
#score
score1=0
score2=0
score= turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0,260)
score.write('Player 1:0 Player 2:0',align='center',font=('courier',24,'normal'))

#functions
def user1_up():
    y= user1.ycor() #set the y coordinates of  the user1
    y+=20 #set the y increase by 20
    user1.sety(y) #set the y of the user1 to the new y coordinate

def user1_down():
    y= user1.ycor()
    y-=20 #set the y to decrease by 20
    user1.sety(y)

def user2_up():
    y= user2.ycor()
    y+=20
    user2.sety(y)

def user2_down():
    y= user2.ycor()
    y-=20
    user2.sety(y)
# keyboard bindings
wind.listen() #tell the window to expect keyboard input
wind.onkeypress(user1_up,'w') #when pressing w the function user1 is invoked
wind.onkeypress(user1_down,'s')
wind.onkeypress(user2_up,'Up')
wind.onkeypress(user2_down,'Down')

# main game loop
while True:
    wind.update() #updates the screen everytime the loop run

    #move the ball
    ball.setx(ball.xcor()+ball.x) #ball starts at 0 and everytime loops run --->+ball.x xaxis
    ball.sety(ball.ycor() + ball.y) #ball starts at 0 and everytime loops run --->+ball.y yaxis

    # border check , top border +300px, bottom border -300px, ball is 20px
    if ball.ycor() > 290: #if ball is at top border
        ball.sety(290) #set y coordinate +290
        ball.y *=-1 #reverse direction, making +ball.y---->-ball.dy

    if ball.ycor() < -290 : #if ball is at bottom bordder
        ball.sety(-290)
        ball.y *=-1

    if ball.xcor() > 390: #if ball is at right border
        ball.goto(0,0) #return ball to center
        ball.x *=-1 #reverse the x direction
        score1+=1
        score.clear()
        score.write('Player 1:{} Player 2:{}'.format(score1,score2), align='center', font=('courier', 24, 'normal'))

    if ball.xcor() < -390: #if ball is at left border
        ball.goto(0,0)
        ball.x *=-1
        score2+=1
        score.clear()
        score.write('Player 1:{} Player 2:{}'.format(score1,score2), align='center', font=('courier', 24, 'normal'))
    #reflection of the ball
    if ((ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()< user2.ycor()+40 and ball.ycor()>user2.ycor()-40)):
        ball.setx(340)
        ball.x*=-1

    if ((ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()< user1.ycor()+40 and ball.ycor()>user1.ycor()-40)):
        ball.setx(-340)
        ball.x*=-1
    if user1.ycor()+50 >300 :
        user1.sety(250)
    if user1.ycor()-50 < -300 :
        user1.sety(-250)
    if user2.ycor()+50 >300 :
        user2.sety(250)
    if user2.ycor()-50 < -300 :
        user2.sety(-250)

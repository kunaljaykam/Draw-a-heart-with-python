from turtle import * 

from turtle import  turtle

color("red")
begin_fill()
left(50)
forward(100)
circle(40, 180)
left(260)
circle(40, 180)
forward(100)

end_fill()

back(-25)

turtle.color('purple')
style = ('Courier', 30, 'italic')
back(-35)
turtle.write('Happy Coding ', font=style, align='center')
turtle.hideturtle()


end_fill()

done()

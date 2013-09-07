import turtle

amrita = turtle.Turtle()
amritas_screen = turtle.Screen()
penclr = raw_input("what color should the turtle be?\r\n  --->  ")
pensize = raw_input("what size should the turtle be?\r\n  -->   ")
amrita.pensize(pensize)
amrita.pencolor(penclr)
while True:
  amrita.fd(300)
  amrita.right(90)

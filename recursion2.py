# recursion
import turtle

def spiral(t,d,w,tn):
	t.color("#00B2FF")
	t.width(w)
	t.fd(d)
	t.rt(tn)
	d = d + 0.5
	w = w + 0.10
	tn = tn + 0.25
	if (d < 90):
		spiral(t,d,w,tn)
	#stop recursion
	t.color("#000000")
	#t.width(1)
	#t.bk(d)
	t.circle(d)
	
	

def main():
	screen = turtle.Screen()
	t = turtle.Turtle()
	t.penup()
	t.goto(-75,50)
	t.pendown()
	#spiral(turtle,distance,width,turn)
	spiral(t,1,1,1)
	screen.exitonclick()	
	
if __name__=="__main__":
	main()



'''
#turtle.tracer(0, 0)


	#print(dist)
#turtle.update()

https://docs.python.org/2/library/turtle.html#turtle.delay

screen.tracer(8, 25)
>>> dist = 2
>>> for i in range(200):
...     fd(dist)
...     rt(90)
...     dist += 2

'''

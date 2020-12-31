from graphics import *

win = GraphWin("Samson & the Phillistines", 1020, 660)
win.setBackground("black")
message = Text(Point(510,20), "Son Vs Philistines").draw(win)
message.setSize(24)
message.setStyle("bold")
message.setFill("black")


cam_image = Image(Point(500,420), "Lscape.gif")
cam_image.draw(win)
cam_image2 = Image(Point(880,420), "Samson.gif")
cam_image2.draw(win)
cam_image3 = Image(Point(250,420), "Goliath.gif")
cam_image3.draw(win)

#inputBox = Entry (Point (510 , 20) , 25)
#inputBox.setTextColor("green")
#inputBox.draw(win)




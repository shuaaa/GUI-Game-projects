#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:58:14 2020

@author: olamijojo
"""
from graphics import *

#def createWindow():
    # Creates a 500x500 window titled "Linear Regression" and draws
    #    a "Done Button" in the lower left corner. The window coords
    #    run from 0,0 to 10,10, and the upper right corner of the button
    #    is located at (DoneX, DoneY).
    # Returns the window.
   

# Use Rectangle object to draw the thumbnails
def Thumbnails():
    win = GraphWin("GameLet", 1300, 840)
    #doneButton = Rectangle(Point(.05,0), Point(1, 0.75))
    #doneButton.draw(win)
    message = Text(Point(650, 20),"Prototype for Gamelet")
    message.draw(win)
    
    #Text(doneButton.getCenter(), "Done").draw(win)
    

    #win = GraphWin("GameLet", 1300, 840)
    thumbnails = Rectangle(Point(40,80), Point(185,250))
    thumbnails.draw(win)
    thumbnails.setOutline("blue")
    Text(thumbnails.getCenter(), "QUIZ 1").draw(win)
    #cam_image = Image(Point(112.5,165), "cam1.gif")
    #cam_image.draw(win)
    #red, green, blue = cam_image.getPixel(445,555)
    #cam_image.setPixel(445,555, "pink")
    #cam_image.setPixel(0,0, "blue")
    #win.setBackground("pink")

    sec_thumbnail = thumbnails.clone() #an exact clon of 1st thumbnail
    sec_thumbnail.move(165,0)
    sec_thumbnail.draw(win)
    Text(sec_thumbnail.getCenter(), "QUIZ 2").draw(win)
    
    second_thumbnail = thumbnails.clone() #an exact clon of 1st thumbnail
    second_thumbnail.move(330,0)
    second_thumbnail.draw(win)
    Text(second_thumbnail.getCenter(), "QUIZ 3").draw(win)

    third_thumbnail = thumbnails.clone() #an exact clon of 1st thumbnail
    third_thumbnail.move(495,0)
    third_thumbnail.draw(win)
    Text(third_thumbnail.getCenter(), "QUIZ 4").draw(win)

    fourth_thumbnail = thumbnails.clone() #an exact clon of 1st thumbnail
    fourth_thumbnail.move(660,0)
    fourth_thumbnail.draw(win)
    Text(fourth_thumbnail.getCenter(), "QUIZ 5").draw(win)

    fifth_thumbnail = thumbnails.clone() #an exact clon of 1st thumbnail
    fifth_thumbnail.move(825,0)
    fifth_thumbnail.draw(win)
    Text(fifth_thumbnail.getCenter(), "QUIZ 6").draw(win)

    sixth_thumbnail = thumbnails.clone() #an exact clon of 1st thumbnail
    sixth_thumbnail.move(990,0)
    sixth_thumbnail.draw(win)
    Text(sixth_thumbnail.getCenter(), "QUIZ 7").draw(win)
    
    
    return win

def getPoint(w):
    # w is a GraphWin
    # Pauses for user to click in w. If user clicks somewhere other than
    #    the Done button, the point is drawn in w.
    # Returns the point clicked, or None if user clicked the Done button
    p = win.getMouse()
    if p.getX() < 165 or p.getY() <= 125:
        p.draw(win)
        return quiz1()
    else:
        return None
    
def quiz1():
    
    win = GraphWin("GameLet", 1300, 840)
    message1 = Text(Point(165, 50),"What is the capital of California?")
    message1.draw(win)
    
    #OptionsA, B, C
    ButtonA = Rectangle(Point(85,80), Point(165, 95))
    ButtonA.draw(win)
    Text(ButtonA.getCenter(), "San Francisco").draw(win)
    
    ButtonB = ButtonA.clone()
    ButtonB.move(85,0)
    ButtonB.draw(win)
    Text(ButtonB.getCenter(), "Los Angeles").draw(win)

    ButtonC = ButtonB.clone()
    ButtonC.move(85, 0)
    ButtonC.draw(win)
    Text(ButtonC.getCenter(), "San Mateo").draw(win)
    
def correct():
    p = win.getMouse()
    if p.getX() <= 165 or p.getY() <= 95:
        #p.draw(win)
        message.setText("Click anywhere to quit.")
        return quiz1()
    else:
        return None

    ans = input("What is the capital of Carlifornia?: ")
    if ans != "San Francisco":
        print("wrong Answer")
    else:
        print("Correct")

def insert_img():
    pass


def main():
  # createWindow()
    Thumbnails()
    quiz1()
    
main()
 

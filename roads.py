from graphics import *
import time

def draw_vertical(win, road_width, x_width, y_width, no_of_lanes=1):
    # Draw vertical central line 
    line = Line(Point(x_width/2, 0), Point(x_width/2, y_width))
    line.setOutline('black')
    line.setWidth(2)
    line.draw(win)

    # Draw vertical lanes

    # Left side
    line = Line(Point(x_width/2-road_width, 0), Point(x_width/2-road_width, y_width/2-road_width))
    line.setOutline('black')
    line.setWidth(4)
    line.draw(win)

    line = Line(Point(x_width/2-road_width, y_width/2+road_width), Point(x_width/2-road_width, y_width))
    line.setOutline('black')
    line.setWidth(4)
    line.draw(win)

    # Right side
    line = Line(Point(x_width/2+road_width, 0), Point(x_width/2+road_width, y_width/2-road_width))
    line.setOutline('black')
    line.setWidth(4)
    line.draw(win)

    line = Line(Point(x_width/2+road_width, y_width/2+road_width), Point(x_width/2+road_width, y_width))
    line.setOutline('black')
    line.setWidth(4)
    line.draw(win)


def draw_horizontal(win, road_width, x_width, y_width, no_of_lanes=1):
    # Draw horizontal central line
    line = Line(Point(0, y_width/2), Point(x_width, y_width/2))
    line.setOutline('black')
    line.setWidth(2)
    line.draw(win)

    # Draw horizontal lanes

    # Upper side
    line = Line(Point(0, y_width/2+road_width), Point(x_width/2-road_width, y_width/2+road_width))
    line.setOutline('black')
    line.setWidth(4)
    line.draw(win)

    line = Line(Point(x_width/2+road_width, y_width/2+road_width), Point(x_width, y_width/2+road_width))
    line.setOutline('black')
    line.setWidth(4)
    line.draw(win)

    # Lower side
    line = Line(Point(0, y_width/2-road_width), Point(x_width/2-road_width, y_width/2-road_width))
    line.setOutline('black')
    line.setWidth(4)
    line.draw(win)

    line = Line(Point(x_width/2+road_width, y_width/2-road_width), Point(x_width, y_width/2-road_width))
    line.setOutline('black')
    line.setWidth(4)
    line.draw(win)

def add_car(win, direction, no_of_lanes, x_width, y_width, road_width):
    # No of cars in each road (assuming car_width/2 spacing)
    car_width = road_width/(1/2 + no_of_lanes*3/2)
    car_length = 5/3*car_width
    no_of_cars = (2/3)*(road_width - car_width/2)/car_width
    
    rects = []

    for i in range(no_of_lanes):
        # Top
        if direction == 1:
            rect = Rectangle(Point(x_width/2+car_width/2+i*(1.5)*car_width, car_length/2), Point(x_width/2+3*car_width/2+i*(1.5)*car_width, 3*car_length/2))
            rect.setOutline('brown')
            rect.setWidth(2)
            rect.setFill('red')
            rect.draw(win)

        # Bottom
        elif direction == 3:
            rect = Rectangle(Point(x_width/2-car_width/2-i*(1.5)*car_width, y_width-car_length/2), Point(x_width/2-3*car_width/2-i*(1.5)*car_width, y_width-3*car_length/2))
            rect.setOutline('brown')
            rect.setWidth(2)
            rect.setFill('red')
            rect.draw(win)

        # Left
        elif direction == 4:
            rect = Rectangle(Point(car_length/2, y_width/2-car_width/2-i*(1.5)*car_width), Point(3*car_length/2, y_width/2-3*car_width/2-i*(1.5)*car_width))
            rect.setOutline('brown')
            rect.setWidth(2)
            rect.setFill('red')
            rect.draw(win)
        
        # Right
        elif direction == 2:
            rect = Rectangle(Point(x_width-car_length/2, y_width/2+car_width/2+i*(1.5)*car_width), Point(x_width-3*car_length/2, y_width/2+3*car_width/2+i*(1.5)*car_width))
            rect.setOutline('brown')
            rect.setWidth(2)
            rect.setFill('red')
            rect.draw(win)

        rects.append(rect)
    return rects
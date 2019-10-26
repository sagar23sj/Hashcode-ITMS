from graphics import *

from roads import *


X_WIDTH = 800
Y_WIDTH = 800

# Oder is N, E, S, W

NO_OF_LANES = 2

ROAD_WIDTH = 150


win = GraphWin('Intersection', X_WIDTH, Y_WIDTH)
win.setBackground('gray')
 
# Draw ver and hori lanes 
draw_vertical(win, ROAD_WIDTH, X_WIDTH, Y_WIDTH)
draw_horizontal(win, ROAD_WIDTH, X_WIDTH, Y_WIDTH)

# Draw cars
#CAR_LEN = 100
#CAR_WID = 50

signals = [0, 0, 1, 0]

# No of cars in each direction
cars = [add_car(win, i, NO_OF_LANES, X_WIDTH, Y_WIDTH, ROAD_WIDTH) for i in range(1, 5)]

t_end = time.time() + 5
NO_OF_SIGNALS=4


inflows=[2,5,1,2]
times=[71.44, 71.4, 96.44, 60.72]

# Update signal state every second
# Update times every cycle

# Update signal state
start_time = time.time()
for j in range(4):

    if time.time() >= start_time + 1:
        start_time = time.time()
        s = signals
        signals = [s[i-1] if i!=0 else s[-1] for i in range(len(s))]

    for i in range(len(signals)):
        if signals[i]:
            index = i
            t_end = time.time() + times[i]/20
            
            while time.time() < t_end:
                for lane in range(len(cars[i])):
                    if i == 0:
                        cars[i][lane].move(0, 5)
                    elif i == 1:
                        cars[i][lane].move(-5, 0)
                    elif i == 2:
                        cars[i][lane].move(0, -5)
                    elif i == 3:
                        cars[i][lane].move(5, 0)




win.close()
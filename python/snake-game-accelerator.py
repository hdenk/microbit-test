import microbit, random
# background oxo grid at brightness 1
gridImg = microbit.Image("00000\n"
                         "00000\n"
                         "00000\n"
                         "00000\n"
                         "00000\n")

# returns False is a square is blank
def check_squares_filled():
    for x in range(5):
        for y in range(5):
            if microbit.display.get_pixel(x,y) == 0:
                return False
    return True
    
def get_grid():
    return [[microbit.display.get_pixel(x,y) for y in range(5)] for x in range(5)]
    
def grid():
    microbit.display.show(gridImg)
    
# returns -2 to 2 from -1024 to +1024, empirically calculated
def tilt_scale(a):
    a = a + 1024 # range 0 to 2048
    a = min(a, 2048)
    a = max(a, 0)
    # < 512 = 0, 512-853(512+341) = 1, 853-1194 = 2, 1194-1536 = 3,  1536-2048 = 4
    if a<512: return -2
    if a<853: return -1
    if a<1194: return 0
    if a<1536: return 1
    return 2
    
def get_tilt():
    x,y,z = microbit.accelerometer.get_values()
    #print(x+1024,y+1024,z+1024)
    x = tilt_scale(x)
    y = tilt_scale(y)
    z = tilt_scale(z)
    #print(x,y,z)
    return x,y,z

def pick_speed(speed):
    while not microbit.button_b.is_pressed():
        microbit.display.show(str(speed))
        if microbit.button_a.is_pressed():
            speed -= 1
            if speed < 1: speed = 9
            microbit.sleep(200)
    return speed

speed = 9 # set default speed
# play game forever
while True:
    # blank screen
    grid()
    end = False
    won = False
    tailJustMissed = False
    score = 0
    xpos = 2 # start in centre
    ypos = 2
    xv = 1 # start going right
    yv = 0
    snake = []
    snake.append((xpos,ypos)) # snake is a list of tuples which are coordinates
    oldBrightness = 0 # start on dark pixel
    foodEaten = True
    foodTimeout = 0
    # pick a speed, A reduces speed, B sets speed
    speed = pick_speed(speed)
    while not end: # run until the game is over
            # loop until randomly found blank square
            while foodEaten or foodTimeout == 0:
                foodX = random.randint(0,4)
                foodY = random.randint(0,4)
                if microbit.display.get_pixel(foodX,foodY) == 0:
                    foodEaten = False
                    foodTimeout = 20
            grid() # blank screen
            microbit.display.set_pixel(foodX,foodY,9) # draw food

            xt,yt,zt = get_tilt()
            # if tilting x more than y, and currently moving in y direction (to avoid going back on yourself), change x
            if abs(xt) > abs(yt) and xv == 0:
                # change x
                if xt > 0: xv = 1
                if xt < 0: xv = -1
                yv = 0
            # if tilting y more than x, and currently moving in x direction (to avoid going back on yourself), change y
            elif abs(yt) > abs(xt) and yv == 0:
                # change y
                if yt > 0: yv = 1
                if yt < 0: yv = -1
                xv = 0

            headx,heady = snake[-1] # old head is last item in snake list
            # new head, mod 5 to wrap around
            newheadx = (headx + xv) % 5
            newheady = (heady + yv) % 5

            for coord in snake[1:]: # draw snake, without new head
                xpos,ypos = coord
                #print(xpos,ypos)
                # make current position max brightness
                microbit.display.set_pixel(xpos, ypos, 5)

            newpixel = microbit.display.get_pixel(newheadx,newheady)
            # if newpixel is 0, 9, or tail of snake
            if (newheadx,newheady) == snake[0]: # if tail of snake, delete tail
                newpixel = 0
                tailJustMissed = True
            else:
                tailJustMisssed = False
            if newpixel == 9 or newpixel == 0: # didn't hit ourself
                snake.append((newheadx,newheady))
                microbit.display.set_pixel(newheadx, newheady, 7)
            else: # did hit ourself
                end = True
            if newpixel == 0: # blank pixel to move to
                if not tailJustMissed:
                    microbit.display.set_pixel(snake[0][0],snake[0][1],0)
                del snake[0]
            elif newpixel == 9: # eaten the food
                foodEaten = True
                score += (10 - speed) # more points for faster game

            # if all the squares are filled the game is won
            squaresFilled = check_squares_filled()
            if squaresFilled:
                won = True
                end = True
            # higher the speed, slower the game
            foodTimeout -= 1
            microbit.sleep(speed*100)
   
    if won:
        microbit.display.scroll("Win "+str(score))
    else:
        microbit.display.scroll("Lose "+str(score))

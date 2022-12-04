import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(1300, 100000)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Climate Change")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-18000, -5, -17.66, 40)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="image/m2.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1275, -600, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("image/hurricane.gif")
    t.shape("image/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()
    file = open('data/global.csv', 'r')
    text = file.readlines()
    for i in range (1, 10):
        line = text[i]
        col = line.split(',')
        temp = float(col[1])
        lat = col[5]
        long = col[6]

        t.pu()
        t.goto(long,lat)
        t.pd()
        t.stamp()
        
        if 'N' in lat:
            lat = lat.replace('N','')
            lat = float(lat[:3])
        if 'S' in lat:
            lat = lat.replace('S','')
            lat = -1* float(lat[:3])
        if 'W' in long:
            long = long.replace('W','')
            long = -1*float(long[:3])
        if 'E' in long:
            long = long.replace('E','')
            long = float(long[:3])
        if -10 < temp <= 0:
            t.color("#FFDAB9")
        if 0 < temp <= 10:
            t.color("#FF7F50")
            
        if 10 < temp <= 20:
            t.color("#FF6347")
            
        if 20 < temp <= 30:
            t.color("#FF4500")
            
        if 30 < temp <= 40:
            t.color("#8B0000")
            
        if 40 < temp <= 50:
            t.color("#FFDAB9")
            
        if 50 < temp <= 60:
            t.color("#DC143C")
            
    wn.exitonclick()
    
        
        
        
    

    # your code to animate Irma here

if __name__ == "__main__":
    irma()


from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd

#################################################################
#  Read .csv, make and analyze dataframe 
#################################################################

# Read in the data
# .csv file has a header.
# index_col default is None.
df = pd.read_csv('BEV.csv')

print(df.head(2))
#Year,BEV sales,Gasoline reduction
#2011,10,1
#2012,15,6

print(df.describe())

years = list(df['Year'])

sales_BEV = list(df['BEV sales'])


# note: years is the same for both datasets
df_PHEV = pd.read_csv('PHEV.csv')
sales_PHEV = list(df_PHEV['PHEV sales'])


#################################################################
#  Create figure, axes, x-axis, y-axis ticks, labels
#################################################################

plt.rcParams.update({'font.size': 14})   # default font size

fig, ax = plt.subplots(
    figsize = (6,6)          # dimensions of the figure in inches
)

# xlim sets the x-axis ticks and tick labels
# ylim sets the y-axis ticks and tick labels
ax.set(xlim=(2010, 2021), xticks=(range(2011, 2021)),
       ylim=(0, 300), yticks=range(50, 251, 50))

# give the x-axis ticks special labels
x_tick_labels = ['2011'] + \
    [f"{i}" for i in range(12,20)] + ['2020']

ax.set_xticklabels(x_tick_labels)

ax.set_ylabel("Sales (thousands)")

# adjust the spacing around and between subplots
fig.subplots_adjust(
    left=0.18,
    bottom=0.20,
    top=0.75)


#################################################################
#  load images of 2 cars
#################################################################

# load images
BEV_img = plt.imread('battery_electric_car.png')
PHEV_img = plt.imread('PH_electric_car.png')

# extent: [left, right, bottom, top]
BEV_axes_img = ax.imshow(BEV_img,
    extent=[2011, 2012, 10, 40], aspect='auto')
PHEV_axes_img = ax.imshow(PHEV_img,
    extent=[2013, 2014, 10, 50], aspect='auto')

CAR_WIDTH = 1

# looks better, due to the way the plug trails in the picture
PH_CAR_WIDTH = 1.1
PH_CAR_X_OFFSET = -0.18

CAR_HEIGHT = 35
CAR_Y_OFFSET = 0

# looks better, so that the car is not floating too high
PH_CAR_Y_OFFSET = -3


def move_cars(x, y, y2):
    # extent: [left, right, bottom, top]
    BEV_axes_img.set_extent((x, x + CAR_WIDTH, 
        y + CAR_Y_OFFSET,
        y + CAR_Y_OFFSET + CAR_HEIGHT))

    PHEV_axes_img.set_extent((x + PH_CAR_X_OFFSET, x + PH_CAR_WIDTH, 
        y2 + PH_CAR_Y_OFFSET,
        y2 + PH_CAR_Y_OFFSET + CAR_HEIGHT))


#################################################################
#  Plot the first line
#################################################################

# ax.plot() returns a list of Line2D (the lines that will be drawn).
# use [0] to get the first line in the list.

line = []
line1 = ax.plot([], [], color='b', lw=2,
    label='BEV (battery electric vehicles)')[0]
    
line.append(line1)
line1 = ax.plot([], [], color='r', lw=2,
    label='PHEV (plug-in hybrid electric vehicle)')[0]
line.append(line1)

# RETURN line 
def init():
    line[0].set_data([], [])
    line[1].set_data([], [])
    return line


# initializing empty values
# for x and y co-ordinates
xdata, ydata, y2data = [], [], []

# interpolate bet data points
SEG = 20  # number of segments between data points


#################################################################
#  Update the line
#################################################################

# animation function
# IN: i:  is the frame number
# More args may be passed via FuncAnimation()'s fargs parameter
#
# OUT: return lines with all the x,y data to be drawn for frame i
def animate(i):
    print(f"animate():  frame #i is {i}")    # 0 .. (MAX_FRAMES - 1)
    # we don't want current_index or last_index to go outside of 0..9
    # Hence we set MAX_FRAMES.

    if (i%SEG == 0):
        # x,y and x,y2 will be plotted
        curr_index = int(i/SEG)
        x = years[curr_index] 
        y = sales_BEV[curr_index] 
        y2 = sales_PHEV[curr_index] 


    elif (i/SEG + 1 < 10):
        # interpolate bet last data point and next data point
        last_index = int(i/SEG)
        last_x = years[last_index]
        last_y = sales_BEV[last_index]
        last_y2 = sales_PHEV[last_index]

        next_index = last_index + 1 
        next_x = years[next_index]
        next_y = sales_BEV[next_index]
        next_y2 = sales_PHEV[next_index]

        x = ((next_x - last_x) * (i%SEG) / float(SEG)) + last_x
        y = int((next_y - last_y) * (i%SEG) / float(SEG)) + last_y
        y2 = int((next_y2 - last_y2) * (i%SEG) / float(SEG)) + last_y2

    else:
        print(f"ERROR")
        next_x = years[ int(i/SEG) + 1]   # generates IndexError,
        # so need to make number of frames smaller in FuncAnimation()


    move_cars(x, y, y2)

    # Each time animate() is called, the lists (xdata, ydata, and 
    # ydata) increase in length by 1
    xdata.append(x)
    ydata.append(y)
    y2data.append(y2)

    # line contains all of the lines, which each contain points 
    line[0].set_data(xdata, ydata)
    line[1].set_data(xdata, y2data)

    return line


#################################################################
#  FuncAnimation
#################################################################

'''
Store the created Animation in a variable that lives as long as the
animation should run. Otherwise, the Animation object will be
garbage-collected and the animation stops.
'''

MAX_FRAMES = SEG * 9 + 1

# repeatedly call the animation function 'animate' for MAX_FRAMES times
anim = FuncAnimation(fig, 
    animate,              # set the animation function
    init_func = init,

    frames = MAX_FRAMES,  # necessary if exporting the file

    # delay between each frame in millisec.  
    # default is 100.
    # note: this is overridden by the fps in anim.save()
    interval = 25,

    # blit is True,
    # this "returns an iterable of all artists that are to be modified or created"
    # "This data is used by the blitting algorithm to decide which parts of the
    # figure has to be update."
    blit = True)


####################################################################
#  Title
####################################################################

# main title above everything else
plt.suptitle("Electric Vehicle Sales in US", 
    fontsize=24,
    fontweight='bold',
    va='top')


####################################################################
#  Footer
####################################################################

plt.figtext(0.069, 0.02,
    "Data: Gohlke and Zhou (2021) Assessment of Light-Duty Plug-in Electric\nVehicles in the United States (2010 - 2020) doi:10.2172/1785708\nCar Drawings: stockgiu / vecteezy.com   Viz: @roannav",
    ha="left",
    fontsize=10)


####################################################################
#  Legend
####################################################################

# bbox = bounding box
# bbox_to_anchor( x, y):  x,y is the location of the legend
plt.legend( bbox_to_anchor=(-0.01, 1.04),
    loc='lower left',
    frameon=False,     # remove border
    borderpad=0,       # remove padding just inside the border
    handleheight=1.5,  # default height is 0.7
    fontsize=12)


#################################################################
#  Save animation
#################################################################

# save animation to local MP4 file 
#anim.save('anim_ffmpeg.mp4', writer = 'ffmpeg', fps = 15)

# save looping animation to local GIF file.
anim.save('anim_imagemagick.gif', writer='imagemagick', fps = 15) 

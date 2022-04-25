import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap
import numpy as np
import data


#############################################################
#  Get Data 
#############################################################

# 24 rows, 365 col.  Each cell gets a random int [0..10)
#X = (10*np.random.rand(24,365)).astype(int)  # for testing
X = data.get_data()

numrows, numcols = X.shape
print(f"numrows={numrows}, numcols={numcols}")


#############################################################
#  Custom Colormap
#  Want more color varieties at the bottom part of the colormap.
#############################################################

# cm.jet     # bright rainbow
colors_jet = cm.jet(np.linspace(0.4,1,80))  # use just the top 60%
#print("The last color in colors_jet is", colors_jet[-1])

maroon = np.array([0.5,0,0,1])
colors_maroon = np.tile(maroon, (176,1))

# On top of the truncated jet colormap, stack the maroon color 
jet_maroon = np.vstack(( colors_jet, colors_maroon))

# white will mean there was NO DATA or a 0 or negative value.
# Replace the very beginning of the colormap with the white color.
# The selected slice is [ first row, every column]
jet_maroon[:1, :] = np.array([1,1,1,1])  # white
 
# make the np.ndarray of colors into a colormap
new_colormap = ListedColormap( jet_maroon)


#########################################################################
#  Create the plot 
#########################################################################

# This code uses the OO-style matplotlib, using subplots().
fig, ax = plt.subplots(
    figsize = (16,9)          # dimensions of the figure in inches
)

# imshow:  displays data as an image (2D)

# vmin, vmax:
# When using scalar data and no explicit norm, vmin and vmax 
# define the data range that the colormap covers. 
# *** By default, the colormap covers the complete value range 
# of the supplied data. ***
# It is an error to use vmin/vmax when norm is given. 
# When using RGB(A) data, parameters vmin/vmax are ignored.

im = ax.imshow(X, 
    # cmap is expecting a named colormap, not an array of colors
    cmap=new_colormap, 

    # aspect:  by default pixels are square
    aspect=3,  # makes a pixel 3x as tall as it is wide
    interpolation='nearest')


#########################################################################
#  x-axis and y-axis
#########################################################################

# remove tick marks, but leave tick labels
plt.tick_params(left=False)
plt.tick_params(bottom=False)

ax.xaxis.set_tick_params(rotation=90)

labels = ['midnight', '', '', '', '4 am', '', '', '', '8 am', '', '', '', 'noon', '', '', '', '4 pm', '', '', '', '8 pm', '', '', '11 pm']

ax.set_yticks( range(24), labels = labels)

labels = [''] * 365
label_strings = ("Jan 1", "Feb 1", "Mar 1", "Apr 1", "May 1", 
    "Jun 1", "Jul 1", "Aug 1", "Sep 1", "Oct 1", "Nov 1", "Dec 1", 
    "Dec 31")

for l in label_strings:
    ind = data.convert_from_date_str_to_day_of_year( l + ", 2021") - 1
    labels[ind] = l


ax.set_xticks( range(365), labels = labels)


#########################################################################
#  Subplots_adjust 
#########################################################################

# adjust the spacing between subplots
plt.subplots_adjust(left=0.05,     # making this lower, will make
                                   # the main plot move to the left

                    right=0.97, 

                    bottom=0.2,    # making this lower, will move
                                   # the main plot lower

                    top=0.78,       # making this lower, will make 
                                    # the main plot's top be lower
                                    # and move the entire plot down
                    )


#########################################################################
#  Colorbar
#########################################################################

# Create a new axes to the current figure and make it the current axes.
cax = plt.axes(
    # [left, bottom, width, height]  in normalized (0,1) units
    [0.54, 0.69, 0.42, 0.02 ],  # put it, horizontally, above chart 
    #[0.96, 0.1, 0.009, 0.8],  # put it, vertically, on the right side

    title = "PM" + r"$_{2.5}$" + " concentration (µg/m" + r"$^3$)",

    # x tick labels will automatically be given the range of the 
    # values that are in the main image.
    # So don't need to set xticklabels
)

plt.colorbar(im,  # This image is described by the colorbar.
    cax=cax,      # The colorbar will be drawn into this axes.
    orientation='horizontal')


#########################################################################
#  Title Area
#########################################################################

# main title above everything else
plt.suptitle("Air Quality", 
    fontsize=26,
    fontweight='bold'
)

# text just below the title, left column
plt.figtext(0.05, 0.9,
    "This tile chart shows the air quality of EVERY HOUR in 2021.  Each row represents\na specific hour.  Each column represents a single day.\n\nAqua and green is good air, while yellow is some air pollution, and orange, red,\nand maroon are bad air pollution.  Missing values and values <= 0 are white tiles.\n\nThe air quality being measured is PM" + r"$_{2.5}$" + ", which is a kind of fine particle pollution,\nwhich can lead to heart attacks, strokes, and lung problems.",
    ha="left",
    va="top",
    fontsize=12)

# text just below the title, right column
plt.figtext(0.54, 0.9,
    "The data is for Mira Loma, a city in Riverside County, CA, USA.\n\nThe U.S. Environmental Protection Agency (EPA) recommends limits of 12 µg/m" + r"$^3$" + "\n(on average over 3 years) or 35 µg/m" + r"$^3$" + " (over 24 hours) for PM" + r"$_{2.5}$" + ".",
    ha="left",
    va="top",
    fontsize=12)

# alternate micro symbol:  r"$\mu$"


#########################################################################
#  Footer
#########################################################################

# text just below the chart, left column
plt.figtext(0.05, 0.20,
    "Do levels of PM" + r"$_{2.5}$" + " vary from hour to hour?",
    ha="left",
    va="top",
    fontweight="bold",
    fontsize=12)

plt.figtext(0.05, 0.17,
    "This can be determined by seeing if a band of rows has a different color than another\nband of rows.  It looks like the rows around 8am are yellowish (some air pollution),\nwhile rows around 3pm are aqua or green (good air).",
    ha="left",
    va="top",
    fontsize=12)


# text just below the chart, right column
plt.figtext(0.54, 0.20,
    "Do levels of PM" + r"$_{2.5}$" + " vary seasonally?",
    ha="left",
    va="top",
    fontweight="bold",
    fontsize=12)

plt.figtext(0.54, 0.16,
    "Look at the colors of bands of columns.  Some very bad air pollution days occurred\nbetween November and February as seen by the orange and red vertical columns.\nOne notable exception was July 4th - 5th, due to fireworks.",
    ha="left",
    va="top",
    fontsize=12)


# footer
plt.figtext(0.05, 0.03,
    "Data: South Coast AQMD   Viz: @roannav",
    ha="left",
    fontsize=12)


#########################################################################
#  Save or Display Image
#########################################################################

plt.savefig('day23_tiles.png')  # savefig must happen before show()
#plt.show()


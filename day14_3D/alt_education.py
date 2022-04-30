import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import pandas as pd
import numpy as np


############################################################
#  File 1: Read data, make dataframe, and explore data
############################################################

# .csv file has a header.
# index_col default is None.
df1 = pd.read_csv("data/codebook_district.2017.03.15.csv")

print("\nVariables and Definitions\n")
num_rows = df1.shape[0]
for i in range(num_rows):
    row = df1.iloc[[i]]   # row i
    v = row['variable'].values[0]
    d = row['definition'].values[0]
    print(v)
    print("    ", d, "\n\n")


############################################################
#  File 2: Read data, make dataframe, and explore data
############################################################

df = pd.read_csv("data/district.2017.03.15.csv")
print(df.head(2), '\n')

print(df.columns, '\n')

print(df.info(), '\n')


############################################################
#  Prep scatterplot data 
############################################################

# IN: col1, col2: dataframe column names
# IN: y_value: fixed y-coordinate
# IN: max_col1, max_col2: used to filter out rows with too high values
# OUT: xs, ys, zs:  3 lists representing,
#      all the x-coordinates, y-coordinates, and z-coordinates
def compare_2_columns( col1, y_value, col2, max_col1, max_col2):
    print(f"\n\nComparing columns {col1} and {col2}")

    #only keep columns 'col1' and 'col2'
    df2 = df[[col1, col2]].copy()
    print(df2.head(), '\n')
    print(df2.info(), '\n')
    print(df2.describe(), '\n')

    print(f"df2 shape: {df2.shape}\n")
    df2.dropna( inplace=True)  # drop rows with missing data
    print("After dropping empty rows")
    print(f"df2 shape: {df2.shape}\n")

    print("Drop rows that have faulty data")
    # eg ANAHEIM UNION HIGH,ANAHEIM,CA has 2691 teacher student ratio

    # drop rows that have a column 1 value that is > max_col1
    if max_col1:
        df2 = df2[df2[col1] <= max_col1]
        print("\nmax_col1: After dropping rows with bad data")
        print(f"df2 shape: {df2.shape}\n")

    # drop rows that have a column 2 value that is > max_col2
    if max_col2:
        toss = list(df2[df2[col2] > max_col2][col2])
        print(f"Throwing out {len(toss)} values:")
        print(toss)

        df2 = df2[df2[col2] <= max_col2]
        print("\nmax_col2: After dropping rows with bad data")
        print(f"df2 shape: {df2.shape}\n")

    xs = list(df2[col1])
    ys = np.zeros(len(xs)) + y_value
    zs = list(df2[col2])  
    return xs, ys, zs


#x-axis:
#gradRate_reg  # graduation rate
#gradRate_alt

#y-axis:
#puptch_reg   # teacher student ratio
#puptch_alt

# For regular schools,
# graduation rate vs. teacher student ratio
xs, ys, zs = compare_2_columns( 'gradRate_reg', 0.1, 'puptch_reg',
                                None, 200)

# For alt schools,
# graduation rate vs. teacher student ratio
xs2, ys2, zs2 = compare_2_columns( 'gradRate_alt', 0.98, 'puptch_alt',
                                   None, 200)


############################################################
#  Colors 
############################################################

OldLace = '#FFF1E0'
FrostedGlass = '#a8ccd7'
Glass = '#f6feff'


############################################################
#  Plot Figure
############################################################

fig = plt.figure(
    facecolor=OldLace
)
#fig.set_figheight(8)   # dimensions of the figure in inches
#fig.set_figwidth(10)

ax = fig.add_subplot(111, projection='3d', 
    # force matplotlib to use my zorder settings
    computed_zorder=False) 

ax.set_facecolor(OldLace)

# adjust the spacing around or between subplots
fig.subplots_adjust(
    bottom=0.1,
    top=0.85
)


############################################################
#  2 Backdrop Planes
############################################################

rects = [[(0, 0), (0, 120), (100, 120), (100, 0)]] * 2

facecolors = [FrostedGlass, FrostedGlass]

poly = PolyCollection(rects, facecolors=facecolors, 
    alpha=0.6, zorder=0.1)

ax.add_collection3d(poly, zs=[0.11, 0.99], zdir='y')


############################################################
#  Grid, Axis, Ticks, Labels
############################################################

ax.set( xlim=(0, 112), 
        ylim=(0, 1),
        zlim=(0, 200))

# scatter plot and axis labels
ax.text(0, 0.10, 62, "Regular schools", 'x', color='blue')
ax.text(0, 0.98, 59, 'Alternative schools', 'x', color='red')
ax.text(40, -0.22, 0, "graduation rate", 'x', color='blue')
ax.text(40, 0.62, 0, "graduation rate", 'x', color='red')
ax.text(104, 0.99, 0.2, "student to teacher ratio", 'z', color='red')

# to hide all spines, tick marks, tick labels, and the grey box walls
# to leave only the simplified picture
#ax.axis('off')

ax.grid(False)

x_tick_labels = ["0%", "50%", "100%"]
ax.set_xticks( range(0,112,50), labels = x_tick_labels)

# remove y ticks (and y tick labels)
ax.set_yticks([])

z_tick_labels = ["0", "50", "100", "150", "200"]
ax.set_zticks( range(0,201,50), labels = z_tick_labels)

# Avoid, since this causes a UserWarning: 
# FixedFormatter should only be used together with FixedLocator
# ax.set_zticklabels(z_tick_labels) 


############################################################
#  Scatter Plots
############################################################

ax.scatter(xs,ys,zs, color='blue', alpha=0.3, zorder=2.5)
ax.scatter(xs2,ys2,zs2, color='red', alpha=0.3, zorder=2.5)


############################################################
#  Text 
############################################################

# Header
plt.figtext(0.07, 0.85,
    "Alternative schools have lower graduation rates and\nsometimes higher student teacher ratios than regular\nschools.  (US school districts, 2013-14)",
    ha='left',
    fontsize=14,
    color='grey')

# Footer
plt.figtext(0.07, 0.02,
    "Data: ProPublica   Viz: @roannav",
    ha="left",
    fontsize=10,
    color='grey')


############################################################
#  Save to output file 
############################################################

plt.savefig('education.png')

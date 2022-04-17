import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# This code uses the OO-style matplotlib, using subplots().
fig, ax = plt.subplots(
    figsize = (8,8)          # dimensions of the figure in inches
)


# x-axis is 1950 .. 2050
ax.set(xlim=(1950, 2051), xticks=(np.arange(1950, 2051, 10)),
       ylim=(0, 4000000), yticks=np.arange(0, 4000000, 500000))


# give the y-axis ticks special labels
lst = list(np.linspace(1,4, num = 6, endpoint=False))
y_tick_labels = ['0', '500,000 tons'] + \
    [(f"{f:.1f}" + " million tons") for f in lst] 

ax.set_yticklabels(y_tick_labels)



img = plt.imread('dark_ocean.jpg') # load image

# extent: [left, right, bottom, top]
ax.imshow(img,  extent=[1950, 2051, 0, 4000000], aspect='auto')



##################################################################
# Read in the data
##################################################################

# .csv file has a header:
# Entity,Code,Year,Accumulated ocean plastic: Microplastics (<0.5cm)
#
# index_col default is None
df = pd.read_csv('microplastics-in-ocean.csv')

print(df.head(2))
print(df.columns)
print(df['Entity'].value_counts())

# 3 different plots, each containing 101 points
# df1 Emissions stop in 2020      101
# df2 Emissions level to 2020     101
# df3 Emissions growth to 2050    101

df4 = pd.read_csv('macroplastics-in-ocean.csv')
print(df4.head(2))
print(df4.columns)
print(df4['Entity'].value_counts())

# 3 different plots, each containing 101 points
# df5 Emissions stop in 2020      101
# df6 Emissions level to 2020     101
# df7 Emissions growth to 2050    101




##################################################################
# Create line plots.  
# Draw them in the order that it will appear in the legend.
##################################################################

df7 = df4[df4['Entity'] == 'Emissions growth to 2050']
x = df7['Year']
y = df7['Accumulated ocean plastic: Macroplastics (>0.5cm)']
ax.plot(x, y, linewidth=4.0, ls = '--', color = 'red',
    label='Macroplastics, if pollution grows through 2050')

df6 = df4[df4['Entity'] == 'Emissions level to 2020']
x = df6['Year']
y = df6['Accumulated ocean plastic: Macroplastics (>0.5cm)']
ax.plot(x, y, linewidth=4.0, ls = '--', color = 'aqua',
    label='Macroplastics, if pollution flattens in 2020')

df5 = df4[df4['Entity'] == 'Emissions stop in 2020']
print("Emissions stop in 2020")
print(df5.describe())
x = df5['Year']
y = df5['Accumulated ocean plastic: Macroplastics (>0.5cm)']
ax.plot(x, y, linewidth=4.0, ls = '--', color = 'lime',
    label='Macroplastics, if pollution ends in 2020')




df3 = df[df['Entity'] == 'Emissions growth to 2050']
x = df3['Year']
y = df3['Accumulated ocean plastic: Microplastics (<0.5cm)']
ax.plot(x, y, linewidth=2.3, ls = ':', color = 'orange',
    label='Microplastics, if pollution grows through 2050')

df2 = df[df['Entity'] == 'Emissions level to 2020']
x = df2['Year']
y = df2['Accumulated ocean plastic: Microplastics (<0.5cm)']
ax.plot(x, y, linewidth=2.0, ls = ':', color = 'yellow',
    label='Microplastics, if pollution flattens in 2020')

df1 = df[df['Entity'] == 'Emissions stop in 2020']
print("Emissions stop in 2020")
print(df1.describe())
x = df1['Year']
y = df1['Accumulated ocean plastic: Microplastics (<0.5cm)']
ax.plot(x, y, linewidth=2.0, ls = ':', color = 'fuchsia',
    label='Microplastics, if pollution ends in 2020')



plt.legend()


# adjust the spacing between subplots
fig.subplots_adjust(
    left=0.22,
    bottom=0.12,
    top=0.59
)

#########################################################################
#  Title Area
#########################################################################

# main title above everything else
plt.suptitle("Plastic Pollution in the Ocean", 
    fontsize=24,
    fontweight='bold'
)

# text just below the title
plt.figtext(0.069, 0.92,
    "Plastic, when not safely disposed of or recycled, may end up in rivers and oceans.\nOver time, large plastic breaks down into smaller macroplastics (> 0.5 cm size)\nand tiny microplastics (< 0.5 cm size).  In the chart, the 3 thicker, dashed lines\nrepresent macroplastics, while the 3 smaller, dotted lines represent microplastics.\n\nThe future of plastic pollution in the ocean could follow 3 paths:\n1) pollution continues to grow to 2050 in line with historic growth rates\n2) pollution continues to grow until 2020, then flattens  *\n3) pollution stops by 2020  *\n \n* Even if we prevented future pollution, the numbers of macroplastics and\nmicroplastics will continue to grow for decades, due to the breakdown of larger\nplastics already in shorelines and surface waters.",
    ha="left",
    va="top",
    fontsize=12)


#########################################################################
# Footer
#########################################################################

plt.figtext(0.069, 0.02,
    "Data: https://ourworldindata.org/plastic-pollution   " + \
    "Photo: Alex Dukhanov/Unsplash   Viz: @roannav",
    ha="left",
    fontsize=10)


plt.savefig('plastics.png')  # savefig must happen before show()
#plt.show()

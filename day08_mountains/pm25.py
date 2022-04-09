import pandas as pd
from joypy import joyplot

# https://matplotlib.org/stable/tutorials/colors/colormaps.html
from matplotlib import cm    # colormaps

import matplotlib.pyplot as plt

df1 = pd.read_csv("SanBernardino_PM2_5_A.csv")
df2 = pd.read_csv("SanBernardino_PM2_5_B.csv")
df = pd.concat([df1, df2])

# make a ridgeline plot of pm2.5 levels in Central San Bernardino Mountains 
# during 2021.

#print(df.head())
#print(df.info())
num_rows = df.shape[0]

# You can't have a negative number of Particulate Matter (PM 2.5).
# < 0 values don't make sense, so remove them.
df = df[df['Value']>=0]
print(f"{num_rows - df.shape[0]} rows were deleted")


# Extract the month part from the "Date Time" column.
# Use regular expression to save the 1st digit and optional 2nd digit 
# and discard the rest of the "Date Time".
month = df["Date Time"].astype(str).replace(r'^(\d)(\d?)/(.*)$', r'\g<1>\g<2>', 
    regex=True)

# add a column "Month" to the dataframe
df["Month"]=month

# want ridgeline plot to sort the Month categories by number; not alphabetically
# so convert the values in Month from string to int
df = df.astype({'Month':'int'})

#split it by months; a new density plot for each month.
fig, ax = joyplot(df, by='Month', column='Value',
    # other colormaps: bone, Purples, cividis, cool, twilight, twilight_shifted
    colormap =cm.twilight_shifted, fade = True,
    range_style='own',  # horizontal line under the ridgeline is only visible
                        # where the density is non-zero; 
                        # it doesn't span the whole x-axis
    figsize = (10,6)    # dimensions of the figure in inches
)
plt.xlabel("PM 2.5")


# plt.annotate():
# first arg: text to display
# xy: location being annotated
# xytext: location of the text

plt.annotate('"Peak fire" in San Bernardino, CA\non 6/28/2021?', 
             xy=(200, 0.5), xytext=(230, 0.55),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.annotate('Unknown cause', 
             xy=(320, 0.35), xytext=(250, 0.4),
             arrowprops=dict(facecolor='black', shrink=0.05))

#move main title up
plt.subplots_adjust(top=.82)
plt.suptitle('Distribution of PM 2.5 Levels in Central San\nBernardino Mountains (CA) for Each Month in 2021', fontsize=20)

plt.subplots_adjust(left =.08)
plt.subplots_adjust(bottom=.15)

# description text
plt.text(90,
    0.75,
    "Fine particulate matter (PM 2.5) is an air pollutant.  At high levels,\nit makes the air appear hazy.  High exposure in individuals can\naffect lung function and worsen asthma and heart disease.\nPM 2.5 is caused by vehicle exhausts, burning of fuels, fires,\npower plants, volcanic eruptions and tobacco smoke.",
    fontsize=12)

# footer (credits)
plt.text(0,
    -0.2,
    "Data: South Coast AQMD   Viz: @roannav",
    ha="center",  # horizontalalignment
    fontsize=10)


plt.savefig('fig.png')  # savefig must happen before show()
#plt.show()


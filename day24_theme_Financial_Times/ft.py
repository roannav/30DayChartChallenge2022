import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager


############################################################
#  Read data, make dataframe, and explore data
############################################################

# .csv file has a header.
# index_col default is None.
df = pd.read_csv("out-of-school-children-of-primary-school-age-by-world-region.csv")

print(df.head(2), '\n')

#        Entity Code  Year  Children out of school, primary
#0  Afghanistan  AFG  1974                          1445969
#1  Afghanistan  AFG  1993                          1979198

df.rename(columns = {'Children out of school, primary':'Children'}, inplace = True)

print(df.info(), '\n')

#RangeIndex: 6457 entries, 0 to 6456
#Data columns (total 4 columns):
# #   Column    Non-Null Count  Dtype 
#---  ------    --------------  ----- 
# 0   Entity    6457 non-null   object
# 1   Code      4439 non-null   object
# 2   Year      6457 non-null   int64 
# 3   Children  6457 non-null   int64 

# So there are no null values in the Entity, Year, and Children columns

num_rows = df.shape[0]
print(f"num_rows is {num_rows}\n")  # 6457

#print(df['Entity'].unique(), '\n')

# let's look at these 7 regions
region = {
                                              # similar to FT colors
    'South Asia': '#F83',                     # Mandarin (orange)  
    'North America': '#593380',               # Velvet (violet)
    'Middle East & North Africa': '#96CC28',  # Wasabi (lime)
    'Latin America & Caribbean': '#0F5499',   # Oxford (blue)
    'Europe & Central Asia': '#FF7FAA',       # Candy (pink)
    'East Asia & Pacific': '#990F3D',         # Claret (pink-red)
    'Sub-Saharan Africa': '#0D7680',          # Metallic Seaweed (teal)
} 



# to verify graph accuracy 
def print_values_for_year( year):
    # select just the rows with the specified year
    df_year = df[df['Year'] == year]

    for reg in region.keys():
        # then select just the row with the specified region
        series = df_year.loc[df_year['Entity'] == reg, 'Children']
        if not series.empty:
            print(f"    For {year} in {reg} ... Children = {series.values[0] / 10**6:.2f} million\n")


def print_data_for_several_years():
    for year in [1975, 1980, 1990, 2000, 2010, 2019]:
        print(f"For {year}, what's the no. of children for each region?")
        print_values_for_year( year)

#print_data_for_several_years()


#max_value = max(df['Children'])
#print(f"max value is {max_value} for the world.\n")


############################################################
#  Use Special Font and Font Color 
############################################################

# list fonts on our computer
#print(font_manager.findSystemFonts(fontpaths=None, fontext='ttf'))

font_dir = ['./font/']
font_files = font_manager.findSystemFonts( fontpaths=font_dir)

for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

# tick and text font color
slate = '#262A33' # dark grey


############################################################
#  Plot 
############################################################

# This code uses the OO-style matplotlib, using subplots().
fig, ax = plt.subplots(
    figsize=(8, 6),     # dimensions of the figure in inches
    facecolor='#FFF1E0' # Old Lace
)
ax.set_facecolor('#FFF1E0')

# remove tick marks, but leave tick labels
plt.tick_params(left=False)


y_tick_labels = ["0", "10", "20", "30", "40"]
ax.set_yticks( range(0,50000000,10000000), labels = y_tick_labels)

# Avoid, since this causes a UserWarning: 
# FixedFormatter should only be used together with FixedLocator
# ax.set_yticklabels(y_tick_labels) 


ax.set(xlim=(1975, 2019),
       ylim=(0, 49000000)
)

ax.tick_params(axis='both', colors=slate)
 

for item, color in region.items():
    df2 = df[df['Entity'] == item]
    ax.plot(df2["Year"], df2["Children"], label=item, 
            color=color, linewidth=2.0)

# place the lower left corner of the legend at x,y = 0,0.21
legend1 = ax.legend( loc='lower left',
           bbox_to_anchor=(0., 0.21),
           labelcolor=slate,   # text color
           markerscale=6.0,
           #frameon=False,
           facecolor='#FFF1E0',   
           framealpha=1,       # opaque; not transparent
         )

frame = legend1.get_frame()
frame.set_color('#FFF1E0')


ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid( axis='y', linewidth=0.6, alpha=0.7)


############################################################
#  Black Tag (Rectangle) at the Top 
############################################################

ax.plot([0.07, 0.14],                # Set width of line
        [0.975, 0.975],              # Set height of line
        transform=fig.transFigure,   # Set location relative to plot
        clip_on=False,
        color=slate,
        linewidth=3)


############################################################
#  Text 
############################################################

# font 
plt.rcParams['font.family'] = 'Roboto Condensed'

plt.figtext(0.07, 0.91,
          'Many children are not attending primary school worldwide',
          ha='left',
          fontdict={
              'color': slate,
              'size':16
          })

plt.figtext(0.07, 0.84,
    "Number of children (millions)",
    ha="left",
    fontsize=12,
    color=slate)

# Footer
plt.figtext(0.07, 0.02,
    "Source: Our World in Data   Viz: @roannav",
    ha="left",
    fontsize=10,
    color=slate)

plt.savefig('day24_financial_times.png')

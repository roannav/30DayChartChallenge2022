import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('UNdata_rail_lines.csv')

# So that we aren't looking at so many countries,
# let's just look at those that started and ended
# with less than 5000 km of total rail lines
df = df[df['Value'] < 5000]

# dataframe with just rows, where Year is 1995
df_country_1995 = df[df['Year'] == 1995]

# dataframe with just rows, where Year is 2019
df_country_2019 = df[df['Year'] == 2019]

# keep only countries that have data for both of the years
country_1995 = df_country_1995["Country or Area"]   # Series
country_2019 = df_country_2019["Country or Area"]
countries = sorted(list(set(country_1995).intersection(set(country_2019))))

# Highlight just the ones with highest or lowest
# absolute increase (not necessarily highest or lowest
# rate of increase)
colors = {
    # Countries with a steep increasing slope: Korea and Israel
    "Korea": "green",
    "Israel": "green",

    # Countries with a steep decreasing slope: Latvia and Dem. Rep. Congo
    "Latvia": "red",
    "Dem. Rep. Congo": "red"
}



fig, ax = plt.subplots(1, figsize=(10,10),
    facecolor='lightgrey')
ax.set_facecolor('white')

for i,v in enumerate(countries):
    cntry = df[df['Country or Area'] == v] # a single country
    plt.plot(cntry.Year, cntry.Value,
             color = colors[v] if (v in colors) else "grey",
             lw=2.5, # line width
             marker='o', markersize=5)

    # for overlapping (unreadable) country names,
    # push the country label down
    push_down_left = 0
    if v in ['Bulgaria','Israel']:
        push_down_left = 100
    elif v in ['Tunisia','Vietnam']:
        push_down_left = 50
    elif v in ['North Macedonia']:
        push_down_left = -50  # go up 50

    push_down_right = 0
    if v in ['Bulgaria', 'Slovak Republic']:
        push_down_right = 100
    elif v in ['Greece','Vietnam']:
        push_down_right = 50

    # start label
    plt.text(cntry.Year.values[1]-0.6,
             cntry.Value.values[1] - push_down_left,
             v, ha='right')

    # end label
    plt.text(cntry.Year.values[0]+0.6,
             cntry.Value.values[0] - push_down_right,
             v)

# x limits, x ticks, and y label
plt.xlim(1987,2027)
plt.xticks([1995, 2019])

plt.ylabel('km', fontsize='14')

# get y ticks, replace 1,000 with k, and draw the ticks
yticks = plt.yticks()[0]

# [1:-1] to remove the first and last y ticks
plt.yticks(yticks[1:-1],
           [f'{i/1000}k' for i in yticks[1:-1]])


# vertical lines of grid
ax.xaxis.grid(color='black', linestyle='solid',
              which='both', alpha=0.9)

# horizontal lines of grid
ax.yaxis.grid(color='black', linestyle='dashed',
              which='both', alpha=0.1)

# remove spines
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)

font1 = {'family':'serif','color':'black','size':20}
plt.title('Rail lines (total route)\n', loc='center',
          fontdict=font1)

plt.figtext(0.02, 0.02,
            "Data: World Development Indicators | The World Bank   Viz: @roannav",
            ha="left",  # horizontalalignment
            fontsize=10)

plt.savefig('day05_slope.png')  # savefig must happen before show()
#plt.show()


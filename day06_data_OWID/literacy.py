import pandas as pd
import seaborn as sns

df = pd.read_csv('literacy-rates-of-the-the-younger-population-15-24-years-versus-literacy-rates-of-the-older-population-65.csv')

# remove rows that have a NaN for elderly_rate, youth_rate, or pop
df = df[df['Elderly literacy rate, population 65+ years, both sexes (%)'].notnull()]
df = df[df['Youth literacy rate, population 15-24 years, both sexes (%)'].notnull()]
df = df[df['Population (historical estimates)'].notnull()]

# let's look at years >= 2010
df = df[df['Year'] >= 2010]


sns.set_theme(style="white")

# Plot youth_rate against elderly_rate with other semantics
ax = sns.relplot(
    x='Youth literacy rate, population 15-24 years, both sexes (%)',
    y='Elderly literacy rate, population 65+ years, both sexes (%)',
    hue="Entity",
    size="Population (historical estimates)",
    col="Continent", col_wrap=3,
    sizes=(800, 1200), alpha=.5, palette="muted",
    height=6,
    aspect=1.0,
    data=df)


ax2 = sns.move_legend(
    ax, "upper center",
    bbox_to_anchor=(.5, 0), ncol=8, title="Countries", frameon=False)


#move main title up
ax.fig.subplots_adjust(top=.8)
ax.fig.suptitle('Literacy Rates: Younger vs Older Generation', fontsize=30)

# the comment below the title
ax.fig.text(0.02, 0.90,
    "In every country, for 2010-2016, the younger population (those aged " + \
    "15-24) have higher or equal literacy rates than the older population",
    ha="left",  # horizontalalignment
    fontsize=18)

ax.fig.text(0.02, 0.87,
    "(those aged 65 and older).",
    ha="left",  # horizontalalignment
    fontsize=18)


# footer (credits)
ax.fig.text(0.02,
    -0.36,
    "Data: https://ourworldindata.org/literacy   Viz: @roannav",
    ha="left",  # horizontalalignment
    fontsize=12)


#A global x- or y-label can be set using the FigureBase.supxlabel and FigureBase.supylabel methods.
# Don't write the xlabel for each chart, instead just write it once, below all the charts
ax.set( xlabel = "")
ax.fig.supxlabel('Youth literacy rate, population 15-24 years, both sexes (%)', fontsize=16)

# Don't write the ylabel for each chart, instead just write it once, to the left of all the charts
ax.set( ylabel = "")
ax.fig.supylabel('Elderly literacy rate, population 65+ years, both sexes (%)', fontsize=16)


ax.fig.savefig('fig.png',
    bbox_inches='tight')  # so that the legend and footer are not cut off

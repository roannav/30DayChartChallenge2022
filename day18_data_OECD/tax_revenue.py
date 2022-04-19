import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the data
# .csv file has a header.
# index_col default is None.
df = pd.read_csv('gdp.csv')
#df.head(2)

GDP_df = df[['LOCATION','Value']]
GDP_df = GDP_df.set_index('LOCATION')
GDP_df.rename(columns = {'Value':'GDP'}, inplace = True)

#GDP_df.head()
#GDP_df.describe()


df = pd.read_csv('gross_public_debt.csv')
#df.head(2)

gross_public_debt_df = df[['LOCATION','Value']]
gross_public_debt_df = gross_public_debt_df.set_index('LOCATION')
gross_public_debt_df.rename(columns = {'Value':'gross_public_debt'}, inplace = True)

#gross_public_debt_df.head(2)
#gross_public_debt_df.describe()


df = pd.read_csv('tax_revenue_as_percentage_of_GDP.csv')
#df.head(2)

tax_revenue_df = df[['COU','Country','Value']]   #.copy()
tax_revenue_df = tax_revenue_df.set_index('COU')
tax_revenue_df.rename(columns = {'Value':'tax_revenue'}, inplace = True)

#tax_revenue_df.head(2)
#tax_revenue_df.describe()

#The merge() function performs an inner join by default,
# so only the indexes that appear in both DataFrames are kept.
GDP_and_debt = pd.merge(GDP_df, gross_public_debt_df, left_index=True, right_index=True)

#The merge() function performs an inner join by default,
# so only the indexes that appear in both DataFrames are kept.
combo = pd.merge(GDP_and_debt, tax_revenue_df, left_index=True, right_index=True)

#combo.describe()

# astype(int)  will convert the floats in the numpy array into integers
dot_radii = list((combo['GDP'] / 20000).astype(int))

# This code uses the OO-style matplotlib, using subplots().
fig, ax = plt.subplots(
    figsize = (8,8),          # dimensions of the figure in inches
    facecolor='papayawhip'
)
ax.set_facecolor('antiquewhite')


ax.set(xlim=(0, 200), xticks=np.arange(25, 201, 25),
       ylim=(20, 50), yticks=np.arange(20, 49, 10)
)

x = list(combo['gross_public_debt'])
y = list(combo['tax_revenue'])

scatter = ax.scatter(x, y,
           s=combo['GDP']/200,
           alpha=0.9,
           edgecolors='none',
           c=combo['GDP'],
           cmap='PRGn_r',
           label=combo['Country']
)


# Format the dollar amounts:
# {x:, } to add a comma to every thousand place starting from the right
# .0f  to remove the decimal portion in the formatting
kw = dict(num=5, # max 5 entries in the legend
          fmt="$ {x:,.0f}")

legend1 = ax.legend(*scatter.legend_elements(**kw),
                    loc="lower right", title="GDP per capita")
ax.add_artist(legend1)


for i, label in enumerate(list(combo['Country'])):

    # hand adjust a few labels, so they don't overlap other labels
    cx = cy = 0
    if label == "Finland":
        cy = -0.8
    elif label == 'Czech Republic':
        cx = -41
    elif label == 'Spain':
        cy = 0.3
    elif label == 'Slovak Republic':
        cy = -0.1
    elif label == 'Luxembourg':
        cx = -2
        cy = -0.6

    plt.annotate(label, (x[i], y[i]), 
        xytext=(x[i] + dot_radii[i] + 2 + cx, y[i] + cy))


ax.grid(True)
ax.set_xlabel('Gross Public Debt as % of GDP')
ax.set_ylabel('Tax Revenue as % of GDP')
ax.set_title('Tax Revenue vs Gross Public Debt (as % of GDP)')

# Footer
plt.figtext(0.06, 0.02,
    "Data: OECD   Viz: @roannav",
    ha="left",
    fontsize=10
)


plt.savefig('tax.png')  # savefig must happen before show()
#plt.show()

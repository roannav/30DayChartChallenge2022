import pandas as pd
import matplotlib.pyplot as plt

# .csv file has a header.
# index_col default is None.
df = pd.read_csv('costs-of-66-different-technologies-over-time.csv')

df.rename(columns = {'J. Doyne Farmer and François Lafond (2016)':'Cost'}, inplace = True)

print(df.head(1), '\n')

print(df['Entity'].unique(), '\n')

'''
'AcrylicFiber', 'Acrylonitrile', 'Ammonia', 'Aniline', 'Benzene', 
'BisphenolA', 'CCGT Power', 'Caprolactam', 'CarbonBlack', 
'CarbonDisulfide', 'Cyclohexane', 'Ethanolamine', 'Ethylene', 
'Formaldehyde', 'HydrofluoricAcid', 'IsopropylAlcohol',
'Low Density Polyethylene', 'Magnesium', 'MaleicAnhydride', 'Methanol',
'NeopreneRubber', 'Paraxylene', 'Pentaerythritol', 'Phenol', 
'PhthalicAnhydride', 'PolyesterFiber', 'PolyethyleneHD', 
'PolyethyleneLD', 'Polypropylene', 'Polystyrene', 'Polyvinylchloride',
'Primary Aluminum', 'Primary Magnesium', 'SodiumChlorate', 
'SodiumHydrosulfite', 'Sorbitol', 'Styrene', 'Titanium Dioxide', 
'Titanium Sponge', 'Urea', 'VinylAcetate', 'VinylChloride', 
'Aluminum', 'Crude Oil', 

FOOD:
'Beer (Japan)', 'Corn (US)', 'Milk (US)', 'Refined Cane Sugar', 'Sodium' 

OTHER TECH:
'DNA Sequencing', 'Automotive (US)', 'Electric Range', 
'Free Standing Gas Range', 'Motor Gasoline'

COMPUTERS AND ELECTRONICS:
'Hard Disk Drive', 'Laser Diode', 'Monochrome Television', 
'Transistor', 'DRAM', 

'''


#ENERGY:
#Concentrated solar power (CSP) is an approach to generating electricity through mirrors.

energy = {
    'Photovoltaics': '#F7E598', 
    'Concentrating Solar': '#C54F46', 
    'Wind Turbine (Denmark)': '#96A8B6', 
    'Ethanol (Brazil)': '#48654D', 
    'Geothermal Electricity': '#941d2a',
    'Nuclear Electricity': '#BB7B84',
    'Onshore Gas Pipeline': '#260e05'
} 

# This code uses the OO-style matplotlib, using subplots().
fig, ax = plt.subplots(figsize=(8, 6))
plt.yscale("log")
ax.minorticks_off()
ax.tick_params(axis='both', colors="darkgrey")

y_tick_labels = ["$0", "$1", "$10", "$100", "$1,000", "$10,000"]
ax.set_yticklabels(y_tick_labels)

ax.set(xlim=(1979, 2006),
       ylim=(1, 20000)
)


for item, color in energy.items():
    df2 = df[df['Entity'] == item]
    ax.plot(df2["Year"], df2["Cost"], label=item, 
            color=color, linewidth=4.0)

ax.legend()

ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid( axis='y', linewidth=0.4, alpha=0.5)

plt.title('Energy Technology Costs', loc='center',
          fontdict={'family':'serif','color':'black','size':20})

# Footer
plt.figtext(0.06, 0.02,
    "Data: Our World in Data   Viz: @roannav",
    ha="left",
    fontsize=10,
    color="darkgrey")

plt.savefig('energy_tech_costs.png')  # savefig must happen before show()
#plt.show()

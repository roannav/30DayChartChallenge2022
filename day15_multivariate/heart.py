import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# options are darkgrid, whitegrid, dark, white, or ticks
#sns.set_style("ticks")

# many options such as bright, husl, Set2, dark, deep, etc.
#sns.set_palette("Set2")  

# Use set_theme() to set style and palette at the same time
#sns.set_theme(style="ticks")

df = pd.read_csv("heart_2020_cleaned.csv")

# There is no missing data already
#df = df.dropna()  # drop rows where at least 1 element is missing (eg NaN)
print(df.shape)

print(df.head())
print(df.columns)
print(df.describe())
print(df.info())

# Target: HeartDisease:  can be 'Yes' or 'No'
print(df.HeartDisease.unique())
print(df.HeartDisease.value_counts())

print(df.AgeCategory.value_counts())
print(len(df.AgeCategory.value_counts()))   #13

age_group = { "18-24": 1, "25-29": 2, "30-34": 3, "35-39": 4, "40-44": 5, 
    "45-49": 6, "50-54": 7, "55-59": 8, "60-64": 9, "65-69": 10, 
    "70-74": 11, "75-79": 12, "80 or older": 13
}
df['AgeGroup'] = df['AgeCategory'].apply( lambda x: age_group[x])


print("df.MentalHealth.value_counts()")
print(df.MentalHealth.value_counts())
#plt.hist(df.MentalHealth, bins=30)

df['Smoking'] = df['Smoking'].apply( lambda x: 1 if x=='Yes' else 0)

print("df.Smoking.value_counts()")
print(df.Smoking.value_counts())
#plt.hist(df.Smoking)

# Do you have serious difficulty walking or climbing stairs?  Yes or No
df['DiffWalking'] = df['DiffWalking'].apply( lambda x: 1 if x=='Yes' else 0)

print("df.DiffWalking.value_counts()")
print(df.DiffWalking.value_counts())
#plt.hist(df.DiffWalking)


#To convert from Yes/No to 1/0
#df['HeartDisease'] = df['HeartDisease'].apply( lambda x: 1 if x=='Yes' else 0)



# The dataset is huge: 319795 rows,
# so I'll take a smaller sample size.
# And have even number of HeartDisease 'No' and 'Yes'
# so just 150 of each.
# 
# The target HeartDisease has mostly 'No' and much less 'Yes'
# No     292422
# Yes     27373

groupbyHeartDisease = df.groupby('HeartDisease')
df2 = groupbyHeartDisease.apply( lambda x: x.sample(n=150, random_state=1, replace=True))

print("\n\n")
print(df2.shape)

print(df2.head())
print(df2.columns)
print(df2.describe())
print(df2.info())
print(df2.HeartDisease.value_counts())
print(df2.AgeGroup.value_counts())


# Numerical data:
# MentalHealth:  for how many days during the past 30 days was your mental
#     health not good?  (0-30 days)
#     0 means the best mental health 
# I will use BMI, SleepTime, and AgeGroup

sns.pairplot(df2, hue="HeartDisease", 
    #kind='kde',
    vars=['AgeGroup', 'BMI', 'Smoking'], 
    #vars=['AgeGroup', 'BMI', 'SleepTime', 'MentalHealth', 'Smoking', 'DiffWalking'], 
    plot_kws=dict(alpha=0.5)
)
#    plot_kws=dict(s=80, edgecolor="white", linewidth=2.5, alpha=0.3))

'''
#MYNOTE:  plot text position is different because I'm not using subplots; I'm just using a Seaborn pairplot

#move main title up
plt.subplots_adjust(top=.82)
plt.suptitle('Distribution of PM 2.5 Levels in Central San\nBernardino Mountains (CA) for Each Month in 2021', fontsize=20)

# footer (credits)
plt.subplots_adjust(bottom =.15)
plt.text(0, 0,
    "Data: https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease   Viz: @roannav",
    ha="left",  # horizontalalignment
    fontsize=10)
'''


plt.savefig('heart.png')

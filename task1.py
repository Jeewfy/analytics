import pandas as pd

df = pd.read_csv('wow_war_within_characters_100k.csv')
df[df['level'] > 30]
# print(df.describe())
#columns = df.select_dtypes(include=['Breed']).columns
#unique_counts = df[columns].nunique
#print(unique_counts)
#x = df[['Breed', 'Gender']].nunique()
#print(x)


#y = df[df['Age_in_months'] > 7]
#print(y)
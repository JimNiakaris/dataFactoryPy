import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', None)

fileName = 'titanic_dataset.csv'
df = pd.read_csv(fileName)

# print(df.head(5))
# print(df.isnull().sum())

# age = df['Age'].mean()
# print(age)

# minage = df['Age'].min()
# print(minage)

# survived = df.loc[:9, ['Name','Age','Survived']]
# print(survived)

# notsurvived = df.loc[df['Survived'] == 0,['Name','Age','Survived']]
# print(f'{len(notsurvived)} didnt survive')

# percentage = (len(notsurvived) / len(df) *100) 
# print(percentage)

# notsurvived_info = df.loc[df['Survived'] == 0,['Name','Sex','Pclass']]
# print(notsurvived_info)

# first_rows_columns = df.iloc[:5, :3]
# print(first_rows_columns)

# last = df.tail(10)
# print(last[:8])


#isin 
df_pclass12 = df[df['Pclass'].isin([1,2])]
print(df_pclass12)


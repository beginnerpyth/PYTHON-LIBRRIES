import pandas as pd
#q1
df=pd.read_csv('sales.csv')
df=pd.read_excel('sales.xlsx')
#q2
print(df.loc[0:5])
print(df.columns)
print(df.info)
print(df.describe)
print(df.dtypes)
print(df.isna())
#q3
print(df['date','revenue'])
print(df[df['revenue']>1000])
#q4
print(df[(df['country']=='Japan')&(df['revenue']>500)])
#q5
print(df['product'].str.startswith('A'))
#q6
df['time']=pd.to_datetime(df['date'])
df['year']=df['time'].dt.year

#q7
print(df.groupby(['country'])['revenue'].sum())
print(df.groupby(['product'])['revenue'].mean())
#q8
df['month']=df['time'].month
print(df.groupby(['month'])['revenue'].sum())
#q9
print(df[df['revenue'].isna()])
print(df['revenue'].fillna(0))
#q10
df['total_value']=df['revenue']*df['quantity']
print(df.head())
#q11
merge=pd.merge(df,countries,left_on='country',right_on='country_code',how='left')
print(merge)
#q12
df=pd.to_csv("sales.csv")
df=pd.to_excel('sales.xlsx')

#i think df.iterrows takes alot of time to iterate cause it has to iterate one by one i think
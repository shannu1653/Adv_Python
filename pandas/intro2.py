import pandas as pd

data={
    'names':['shannu','navven','rohith'],
    'marks':[23,34,34]
}

# df=pd.DataFrame(data)
# print(df)
# print(df.loc[0:2])
# print(df.loc[0:3,'marks'])

# df=pd.read_csv("./emp1.csv")
df=pd.read_csv("./orders.csv")

# 📙 4. Data Selection & Filtering
# print(df[df['marks']>23])

# print(df.loc[9,'ENAME'])
# print(df.iloc[0:,1])

#at/iat
# print(df.iat[2,7]) #index at 2-rows 7-column
# print(df.get("empno"))

#query
# print(df)
# print(df.query("ship_mode=='Second Class' and region =='South'"))
# print(df[(df['ship_mode']=='Second Class') | (df['category']==' Furniture')])


#1.profit
# print(df[(df['profit']).between(5,10)])

#2.isnull/null
# print(df.isnull())
# print(df['quantity'].isnull())

#3.data cleaning
#3.1dropna()
# print(df.dropna(axis=0))


#3.2 fillna
# print(df.fillna('fill'))

#3.3 replace()
#print(df.replace(to_replace='Furniture', value="FURNITURE")) #change lowercase to uppercase

#3.4 drop duplicates
print(df.drop_duplicates())


#pandas-->Pandas (Python Data Analysis Library) is an open-source Python 
# library used for data manipulation, cleaning, analysis, and visualization.
#panel data analysis -->pandas full form


import pandas as pd

#1-d -->row/col-->series
#2-d --> both rows and col --> dataframe

data={
    'names':['shannu','navven','rohith'],
    'marks':[23,34,34]
}


# df=pd.DataFrame(data)
# print(data)
# print(df)
# df=pd.Series(data)
# print(type(df))
# print(df)

#csv-->(comma seperated value)

df=pd.read_csv("./emp1.csv")
# df=pd.read_csv("./emp1.csv",header=None) #used to no heading in my data
# print(type(df))
# print(df)


#3.viewing data
#1.Head
# print(df.head()) #by default give top 5 rows
#give cusrtome value by give parameters
# print(df.head(100)) #it returns top 10 rows  ,if we give out range it does not give error it give total value

# print(df.tail()) #by deffult it returns last 5 rows
# print(df.tail(18))


#***Get basic Info :**********

# print(df.info()) #it gives the structure of the data
# print(df.describe()) #it gives the stastical information
# print(df.shape) #it gives  count od=f the  rows and columns
# print(df.columns) #it returns the columns
# print(df.dtypes) #it gives the data type of the every columns details

# ➤ Access columns & rows:*********

# print(df['ENAME']) #retrive singel column data
print(df[['ENAME','HIREDATE']]) #retrive multiple columns
print(df.loc[0]) # retrive single row data 
print(df.iloc[1])
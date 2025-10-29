import pandas as pd
df=pd.read_csv("./orders.csv")

# import matplotlib.pyplot as plt
# df.groupby('product_id')['sales'].sum().plot(kind='bar', color='skyblue')
# plt.title("Sales by Product")
# plt.show()

#1.astype -->to change the data type for the column in the data frame
# print(df)
# df["sales"]=df["sales"].astype(int)
# print(df)

#2.rename()
# new_df=df.rename(columns={"sales":"New_sales"},inplace=True)
# print(df)

# df.rename(columns={"ship_date":"new_ship_date"},inplace=True)
# print(df)

#3.sort_values
# # df.sort_values(by="profit",ascending=True,inplace=True)
# mew_df=df.sort_values(by="ship_date",ascending=True)
# print(mew_df)

#4.value_count
# print(df['quantity'].value_counts())

#5.groupby
# print(df.groupby('quantity')['profit'].mean())

#6.join()
#merge()combine two data frames
df2=pd.read_csv("./orders.csv")
# print(df.merge(df2,on='category'))
# print(df.merge(df2,on='category',how='inner'))
# print(df.merge(df2,on='category',how='left'))
# print(df.merge(df2,on='category',how='right'))
# print(pd.merge(df,df2,how="cross"))

#7.concat
# print(pd.concat([df,df2]))
# print(pd.concat([df,df2],axis=1)) 

#8.pivot_table
print(pd.pivot_table(df, values='sales', index='order_date', aggfunc='mean'))

#why use pivote_tables research


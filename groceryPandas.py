#%%
#import pandas
import pandas as pd

#import grocery data
grocery_data =pd.read_csv("grocery_sales.csv")
print(grocery_data.head())
#fill in missing sales values
#grocery_data.fillna(value={'sales':0}, inplace = True)
#print(grocery_data.head())
#%%
avg_sales = grocery_data['sales'].mean()
grocery_data['sales'].fillna(value = avg_sales,inplace=True)

# Aggregating data: sum
sales_summary = grocery_data.groupby('transaction_date')['sales'].sum()
print(sales_summary)

#plot sales over time
sales_summary.plot(rot=45)
# %%

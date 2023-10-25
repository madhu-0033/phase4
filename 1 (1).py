import pandas as pd

j=pd.read_csv("./dataset/Historical Product Demand.csv")



# Handling missing values
j.dropna(inplace=True)

# Dealing with duplicates
j.drop_duplicates(inplace=True)





# Data filtering (if needed)
j = j[['Product_Category','Date','Order_Demand']]
print(j)


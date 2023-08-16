import pandas as pd
data = pd.read_csv("C:/Users/SPTINT-02/Downloads/matches_1991_2023.csv")
print(data)
print(data.head(5))
print(data.tail(10))
print(data["home_score"])
print(data.info())      
print(data.dtypes)
print(data.count())
      
      
      

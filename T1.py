import pandas as pd;

#constructing a directory
dirc = {
    "Name": ["Alice","Jane","Taylor","Austin","Lily","Joe","May"],
    "Age": [32,24,21,19,24,34,20],
    "Gender": ["F","F","M","M","F","M","F"]
    
}

#converting to dataframe
df = pd.DataFrame(dirc)

#shows top 5 rows
print(df.head()) 
print("----------------------")

#people aged above 24
print(df[df.Age>24])
print("----------------------")

#note iloc prints 2,3 and loc prints 2,3,4
print(df.iloc[2:4])
print(df.loc[2:4])
print("----------------------")

#reset index
tempDf = df.loc[2:4]
print(tempDf)
tempDf.reset_index(inplace=True, drop=True)
print(tempDf)

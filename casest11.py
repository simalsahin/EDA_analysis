"""1. Import The Libraries And Dataset
2. Display Top 5 Rows of The Dataset
3. Check The Last 5 Rows of The Dataset
4. Find Shape of Our Dataset (Number of Rows And Number of Columns)
5. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
6. Check Null Values In The Dataset
7. Check For Duplicate Data and Drop Them
8. Get Overall Statistics About The Dataset
9. Draw Correlation Matrix
10. How Many People Have Heart Disease, And How Many Don't Have Heart Disease In This Dataset?
11. Find Count of  Male & Female in this Dataset
12. Find Gender Distribution According to The Target Variable
13. Check Age Distribution In The Dataset
14. Check Chest Pain Type
15. Show The Chest Pain Distribution As Per Target Variable
16. Show Fasting Blood Sugar Distribution According To Target Variable
17.  Check Resting Blood Pressure Distribution
18. Compare Resting Blood Pressure As Per Sex Column
19. Show Distribution of Serum cholesterol
20. Plot Continuous Variables"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("heart.csv")
df = pd.DataFrame(data)

#6
result = df.isnull().values.any()
#7
result = df.duplicated().values.any()
result = df.drop_duplicates(inplace=True)
#8
result = df.describe()
#9
result = df.corr()
#sns.heatmap(result,annot=True)
#10
result = df["target"].value_counts()
patient = result[1] * 100 / len(df)
non_patient = result[0] * 100 / len(df)
#11
result = df["sex"].value_counts().reset_index()
#sns.barplot(x = result["index"] , y = result["sex"])
# plt.xlabel("sex")
# plt.ylabel("number of patient")
# plt.xticks([0,1],["female","male"])
#12
result = df.groupby("sex")["target"].value_counts()
# sns.countplot(x = df["sex"],hue=df["target"])
# plt.xticks([0,1],["female","male"])
# plt.legend(labels = ["No disease","disease"])
#13
result = df["age"].describe()
#sns.displot(df["age"])
#14
result = df["cp"].value_counts().reset_index()
# sns.barplot(x = result["index"], y = result["cp"])
# plt.xlabel("chest pain types")
#15
# sns.countplot(x = df["cp"], hue=df["target"])
# plt.xlabel("chest pain types")
# plt.legend(labels = ["No disease","disease"])
#16
# sns.countplot(x = df["fbs"],hue=df["target"])
# plt.xlabel("fasting blood sugar")
# plt.xticks([0,1],["fbs < 120","fbs > 120"])
# plt.legend(labels = ["No disease","disease"])
#17
# sns.distplot(df["trestbps"],bins=20)
#18
# result = sns.FacetGrid(df,hue="sex",aspect=4)
# result.map(sns.kdeplot,"trestbps",shade = True)
# plt.legend(labels = ["female","male"])
#19
sns.distplot(df["chol"])
plt.show()
#20
"""Categorical variables, aka discrete variables.These come in only a fixed number of values – like dead/alive, obese/overweight/normal/underweight, Apgar score.
 Continuous variables.These can have any value between a theoretical minimum and maximum, like birth weight, BMI, temperature, neutrophil count"""
categorical_val = [i for i in df.columns if df[i].nunique() <=10]
continuous_val = [i for i in df.columns if df[i].nunique() > 10]
df.hist(continuous_val,figsize=(15,6))
plt.tight_layout()
plt.show()
print(categorical_val)
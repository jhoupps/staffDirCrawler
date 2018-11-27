import pandas as pd

jobs = pd.read_csv("position_data.csv")
money = pd.read_csv("AnnualEmployeeSalary2013thru2017.csv")

merged = jobs.merge(money, on="Name")
merged.to_csv("merged_output.csv", index=False)

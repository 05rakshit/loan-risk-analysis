import pandas as pd
file=pd.read_csv("loan_data.csv")

#Average Interest Rate and Installment per purpose
total=file.groupby("purpose")[["int.rate","installment"]].mean().sort_values(by="int.rate")
print(total)

#Total Defaults per purpose
default = file[file['not.fully.paid']==1]['purpose'].value_counts()
print(default)

#Default Rate per purpose
default_rate = default/file['purpose'].value_counts()
print(default_rate*100)
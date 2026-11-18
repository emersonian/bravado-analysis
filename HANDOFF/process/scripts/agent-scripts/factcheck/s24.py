import pandas as pd
a=pd.read_csv('/home/user/bravado-analysis/Financials/Quickbooks/Audit Log - 2026.csv',dtype=str)
print(len(a)); print(a.head(60).to_string())
a['mon']=a['Date Changed'].str.extract(r'^(\w+)')
print(a.groupby(['mon','User']).size().to_string())

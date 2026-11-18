import pandas as pd
pd.set_option('display.width',250,'display.max_rows',500,'display.max_columns',50,'display.float_format','{:,.2f}'.format)
p='/home/user/bravado-analysis/Financials/Quickbooks/BRAVADO SPICE LLC_Balance Sheet - Quickbooks.xlsx'
x=pd.read_excel(p,header=None)
h=x.iloc[4].astype(str).tolist()
cols=[h.index(k) for k in ['Dec 2023','Dec 2024','Dec 2025','Mar 2026']]
y=x.iloc[5:,[0]+cols].copy(); y.columns=['line','Dec23','Dec24','Dec25','Mar26']
y=y[(y[['Dec23','Dec24','Dec25','Mar26']].fillna(0).abs().sum(axis=1)>0)]
print(y.to_string())

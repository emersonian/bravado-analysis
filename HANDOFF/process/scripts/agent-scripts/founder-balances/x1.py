import pandas as pd, sys
pd.set_option('display.width',300); pd.set_option('display.max_colwidth',60); pd.set_option('display.max_rows',2000)
v=pd.read_excel('/home/user/bravado-analysis/Financials/Quickbooks/BRAVADO SPICE LLC_Balance Sheet - Quickbooks.xlsx',header=None)
h=v.iloc[4].tolist()
cols=[i for i,c in enumerate(h) if str(c) in ('Dec 2019','Dec 2020','Dec 2021','Dec 2022','Dec 2023','Dec 2024','Dec 2025','Mar 2026')]
print(h[-5:])
out=v.iloc[5:,[0]+cols].copy(); out.columns=['acct']+[h[i] for i in cols]
out=out[out.iloc[:,1:].fillna(0).abs().sum(axis=1)>0]
print(out.to_string(index=False))

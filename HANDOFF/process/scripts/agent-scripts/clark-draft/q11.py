import pandas as pd, sys
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',80)
Q='/home/user/bravado-analysis/Financials/Quickbooks/'
d=pd.read_excel(Q+'BRAVADO SPICE LLC_Balance Sheet - Quickbooks.xlsx',header=None)
hdr=d.iloc[4].tolist()
cols=[0]+[hdr.index(c) for c in ('Dec 2023','Dec 2024','Dec 2025','Mar 2026')]
o=d.iloc[5:,cols]; o.columns=['line','Dec23','Dec24','Dec25','Mar26']
o=o[o[['Dec24','Dec25','Mar26']].fillna(0).abs().sum(axis=1)>0]
print(o.to_string())
print(d.iloc[-4:,0].tolist())

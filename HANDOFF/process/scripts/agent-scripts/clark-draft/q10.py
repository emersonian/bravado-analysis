import pandas as pd, sys
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',80)
Q='/home/user/bravado-analysis/Financials/Quickbooks/'
x=pd.ExcelFile(Q+'BRAVADO SPICE LLC_Balance Sheet - Quickbooks.xlsx')
print(x.sheet_names)
for s in x.sheet_names[:3]:
    d=x.parse(s,header=None)
    print(s,d.shape); print(d.iloc[:6,:8].to_string())
d=x.parse(x.sheet_names[0],header=None)
hdr=d.iloc[4].tolist() if d.shape[0]>4 else None
print(hdr[:5], hdr[-5:])

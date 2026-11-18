import pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_rows',500)
for y in (2023,2024,2025):
    f=f'/home/user/bravado-analysis/Financials/Quickbooks/BRAVADO SPICE LLC_Profit and Loss by Month - {y}.xlsx'
    x=pd.read_excel(f,header=None)
    print(y, x.shape)
    for i,r in x.iterrows():
        print(repr(r.iloc[0]), r.iloc[-1])

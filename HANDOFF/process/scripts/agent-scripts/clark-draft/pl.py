import pandas as pd, sys
pd.set_option('display.width',250); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',60)
Q='/home/user/bravado-analysis/Financials/Quickbooks/'
for y in (2024,2025):
    x=pd.read_excel(Q+f'BRAVADO SPICE LLC_Profit and Loss by Month - {y}.xlsx',header=None)
    print(y, x.shape)
    print(x.iloc[:6].to_string())
    # print first col and last col
    print(x.iloc[:, [0, x.shape[1]-1]].to_string())

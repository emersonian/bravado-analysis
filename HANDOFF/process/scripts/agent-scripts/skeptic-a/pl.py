import pandas as pd
pd.set_option('display.width',250,'display.max_rows',500,'display.max_columns',50,'display.float_format','{:,.2f}'.format)
out={}
for y in ['2024','2025','2026']:
    p=f'/home/user/bravado-analysis/Financials/Quickbooks/BRAVADO SPICE LLC_Profit and Loss by Month - {y}.xlsx'
    x=pd.read_excel(p,header=None)
    hi=[i for i in range(10) if 'Total' in x.iloc[i].astype(str).tolist()][0]
    tc=x.iloc[hi].astype(str).tolist().index('Total')
    s=x.iloc[hi+1:,[0,tc]].copy(); s.columns=['line',y]
    s['line']=s['line'].astype(str).str.strip()
    out[y]=s.reset_index(drop=True)
    print(y); print(s[s[y].notna()].to_string())

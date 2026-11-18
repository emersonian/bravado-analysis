from common import *
import openpyxl
p='/home/user/bravado-analysis/Financials/Quickbooks/BRAVADO SPICE LLC_Balance Sheet - Quickbooks.xlsx'
wb=openpyxl.load_workbook(p,data_only=True)
ws=wb.active
rows=list(ws.iter_rows(values_only=True))
hdr=rows[4]
cols={h:i for i,h in enumerate(hdr) if h}
print(list(cols)[-6:])
sel=[f'Dec {y}' for y in range(2019,2026)]+[list(cols)[-1]]
out={}
for r in rows[5:]:
    if r[0]: out[str(r[0]).strip()]=[r[cols[c]] for c in sel]
df=pd.DataFrame(out,index=sel).T
df.to_pickle('bs_export.pkl')
print(df.to_string())

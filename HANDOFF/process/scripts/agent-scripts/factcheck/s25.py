import openpyxl
p='/home/user/bravado-analysis/Jer to Investors/2026-07-22 - All Investors/2026-07-22-Bravado-Cash-Plan-v3-FINAL-LOCKED.xlsx'
wb=openpyxl.load_workbook(p,data_only=True)
print(wb.properties.created, wb.properties.modified)
ws=wb['Debt_Schedule_Ref']
for row in ws.iter_rows(min_row=1,max_row=22,values_only=True):
    print([x for x in row if x is not None][:8])
ws=wb['Audit_Log']
rows=list(ws.iter_rows(values_only=True))
print(len(rows)); 
for r in rows[-6:]: print([str(x)[:200] for x in r if x is not None])

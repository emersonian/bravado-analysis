from ld import *
import openpyxl
for y in (2024,2025):
    wb=openpyxl.load_workbook(f'/home/user/bravado-analysis/Financials/Quickbooks/BRAVADO SPICE LLC_Profit and Loss by Month - {y}.xlsx',data_only=True)
    ws=wb.active
    for row in ws.iter_rows(values_only=True):
        if row[0] and any(k in str(row[0]) for k in ['Net Income','Total Income','Gross Profit','Total Cost of Goods','Net Operating','Salaries','Total Expenses','Reimbursements']):
            print(y,str(row[0]).strip(), row[-1])
print(q[(q.account=='80000 Interest Earned')&(q.y==2024)&(q.amount.abs()>10)][['date','type','name','memo','amount','split']].to_string())
# Mark's Jeremiah equity tie
print('Finaloop cap-dist-draw', 202009.17-21752.30-5330.80)
# QB 2024 year-end due from Jer in Mark: 72195
print(bal('Due from Jer','2024-12-31'), bal("53000 Jer's Draw",'2024-12-31'))
print(q[(q.num=='AJE-397')][['account','date','memo','amount']].to_string())
print(q[(q.num=='CPA AJE 1')][['account','date','memo','amount']].to_string())

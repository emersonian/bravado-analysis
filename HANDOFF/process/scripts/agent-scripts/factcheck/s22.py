import openpyxl, glob
for y in [2023,2024,2025,2026]:
    p=f'/home/user/bravado-analysis/Financials/Quickbooks/BRAVADO SPICE LLC_Profit and Loss by Month - {y}.xlsx'
    wb=openpyxl.load_workbook(p,data_only=True)
    ws=wb.active
    for row in ws.iter_rows(values_only=True):
        if row[0] and isinstance(row[0],str) and row[0].strip().lower() in ('net income','net operating income','total income','gross profit','total other income','net other income'):
            vals=[v for v in row[1:] if v is not None]
            print(y,row[0].strip(), vals[-1] if vals else None)
